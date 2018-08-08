def new(cls, *args, **kwargs):
    if hasattr(cls, "__instance"):
        return cls.__instance
    instance = cls.__old_new__(cls, *args, **kwargs)
    cls.__instance = instance
    return instance


def singleton(cls):
   cls.__old_new__ = cls.__new__
   cls.__new__ = singleton_new
   return cls
