def new(cls, *args, **kwargs):
    if hasattr(cls, "__instance"):
        return cls.__instance
    cls.__instance = cls.__old_new__(cls, *args, **kwargs)
    return cls.__instance


def singleton(cls):
   cls.__old_new__ = cls.__new__
   cls.__new__ = singleton_new
   return cls
