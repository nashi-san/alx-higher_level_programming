class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        self.__dict__[attr] = value
