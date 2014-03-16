from M2Crypto import BIO, Rand, SMIME, X509
import threading
def makebuf(text):
    return BIO.MemoryBuffer(text)

# Make a MemoryBuffer of the message.
buf = makebuf('''some text''')
def threadSMIME():
    # Seed the PRNG.
    Rand.load_file('randpool.dat', -1)

    # Instantiate an SMIME object.
    s = SMIME.SMIME()
    # Load target cert to encrypt to.
    x509 = X509.load_cert('recipient.pem')
    sk = X509.X509_Stack()
    sk.push(x509)
    s.set_x509_stack(sk)

    # Set cipher: 3-key triple-DES in CBC mode.
    s.set_cipher(SMIME.Cipher('des_ede3_cbc'))

    # Encrypt the buffer.
    p7 = s.encrypt(buf)

    # Output p7 in mail-friendly format.
    out = BIO.MemoryBuffer()
    out.write('From: sender@example.dom\n')
    out.write('To: recipient@example.dom\n')
    out.write('Subject: M2Crypto S/MIME testing\n')
    s.write(out, p7)

    print out.read()

    # Save the PRNG's state.
    Rand.save_file('randpool.dat')

for i in range(5):
    t1 = threading.Thread(target=threadSMIME)
    t1.start()
