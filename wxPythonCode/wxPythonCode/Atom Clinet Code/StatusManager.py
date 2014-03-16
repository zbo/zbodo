class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,"_instance"):
            su = super(Singleton,cls)
            cls._instance = su.__new__(cls,*args,**kw)
        return cls._instance

class StatusManager(Singleton):
    class User():
        name=None
        id=None
        info=None




