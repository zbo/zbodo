#!/usr/bin/env python
import threading

import PyKCS11
import M2Crypto
from M2Crypto import Engine, m2, SSL, httpslib, util, Rand, SMIME, X509, BIO, EVP
from M2Crypto.SSL.Connection import _serverPostConnectionCheck

engine_dll = 'engine_pkcs11.dll'
etoken_dll = 'etpkcs11.dll'

def makebuf(text):
    return BIO.MemoryBuffer(text)

class eToken():
    session=None
    tokenSlot=None
    barium_cert=None
    my_pkey=None
    my_cert=None
    ssl_ctx=None
    pkcs11=None
    engine=None
    def __init__(self,engpath=""):
        self.pkcs11 = PyKCS11.PyKCS11Lib()
        self.engpath = engpath
        self.pkcs11.load(engpath + "\\" + etoken_dll)
        self.engine = Engine.load_dynamic_engine('pkcs11',
                                                 self.engpath + "\\" + engine_dll)
        self.engine.ctrl_cmd_string('MODULE_PATH',self.engpath + "\\" + etoken_dll)
        self.engine.init()
        self.info = None
#        for slot in range(0,10):
#            try:
#                xx = self.pkcs11.getTokenInfo(slot)
#                if xx.model.strip() == "eToken":
#                    self.info = xx
#                    self.tokenSlot = slot
#                    break
#            except PyKCS11.PyKCS11Error as e:
#                print e
#                pass
#        if self.info == None:
#            print "eToken not found"
#            raise
#        print "eToken in slot",self.tokenSlot
        self.tokenSlot=2

    def FindMyCert(self, my_cert, obj):
        if (    ([PyKCS11.CKO_CERTIFICATE] ==
                 self.session.getAttributeValue(obj, [PyKCS11.CKA_CLASS]))
                and (['bobtest'] ==
                     self.session.getAttributeValue(obj, [PyKCS11.CKA_LABEL]))):
            if (my_cert == None):
                my_cert = self.session.getAttributeValue(obj,
                                                         [PyKCS11.CKA_VALUE])[0]
            else:
                raise Exception('Excess client certificate in token')
        return my_cert

    def FindPrivateId(self, obj, privkey_id):
        if ([PyKCS11.CKO_PRIVATE_KEY] ==
            self.session.getAttributeValue(obj, [PyKCS11.CKA_CLASS])):
            if (privkey_id == None):
                privkey_id = self.session.getAttributeValue(obj, [PyKCS11.CKA_ID])
            else:
                raise Exception('Excess private keys in token')
        return privkey_id

    def login(self,pin):
        self.session = self.pkcs11.openSession(self.tokenSlot)
        self.session.login(pin=pin)
        random = ''.join(chr(i) for i in self.session.generateRandom(size=1024))
        objects = self.session.findObjects()
        my_cert = None
        privkey_id = None
        for obj in objects:
            print self.session.getAttributeValue(obj, [PyKCS11.CKA_LABEL])
            my_cert = self.FindMyCert(my_cert, obj)
            privkey_id = self.FindPrivateId(obj, privkey_id)
        self.key_id = ''.join(chr(c) for c in privkey_id[0]).encode('hex')
        self.my_cert = X509.load_cert_der_string(''.join(chr(c) for c in my_cert))
        Rand.rand_seed(random)
        #  init the OpenSSL engine and load the user cert & private key
        ssl_key = 'slot_' + str(self.tokenSlot) + '-id_' + self.key_id
        self.my_pkey = self.engine.load_private_key(ssl_key, pin)
        ctx = SSL.Context('sslv23')
        m2.ssl_ctx_use_x509(ctx.ctx,self.my_cert.x509)
        m2.ssl_ctx_use_pkey_privkey(ctx.ctx,self.my_pkey.pkey)

        if not m2.ssl_ctx_check_privkey(ctx.ctx):
            raise ValueError, 'public/private key mismatch'
        ctx.set_verify(SSL.verify_peer, 10)
        self.ssl_ctx = ctx
        print self.my_cert
        print self.my_pkey
        self.session.logout()
        print str(threading.currentThread().name)+" finished"

    def pkcs7_seal(self, text, recip=None,pin="safenet123$"):
        self.session.login(pin=pin)
        if (None==recip): recip=self.barium_cert
        buf = makebuf(text)
        print text
        print buf
        sm = SMIME.SMIME()
        sm.pkey = self.my_pkey
        sm.x509 = self.my_cert
        M2Crypto.EVP.PKey
        p7 = sm.sign(buf)
        x509 = X509.load_cert('recipient.pem')
        stk = X509.X509_Stack()
        stk.push(x509)
        sm.set_x509_stack(stk)
        sm.set_x509_stack(stk)
        sm.set_cipher(SMIME.Cipher('des_ede3_cbc'))
        tmp = BIO.MemoryBuffer()
        m2.pkcs7_write_bio(p7._ptr(),tmp._ptr())
        p7a = sm.encrypt(tmp)
        out = BIO.MemoryBuffer()
        sm.write(out, p7a)
        self.session.logout()
        return out.read()

    def pkcs7_unseal(self, text, sender=None):
        if (None==sender): sender=self.barium_cert
        sm = SMIME.SMIME()
        sm.pkey = self.my_pkey
        sm.x509 = self.my_cert
        bio = BIO.MemoryBuffer(text)
        p7 = SMIME.PKCS7(m2.pkcs7_read_bio_der(bio._ptr()))
        out = sm.decrypt(p7)
        stk = X509.X509_Stack()
        stk.push(sender)
        store = self.ssl_ctx.get_cert_store()
        p7b = makebuf(out)
        p7final = m2.pkcs7_read_bio_der(p7b._ptr())
        return m2.pkcs7_verify0(p7final, stk._ptr(), store._ptr(), 0)

   







