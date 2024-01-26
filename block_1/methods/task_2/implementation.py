from block_1.common import MyException


class ClassFather:
    registered_list = []

    @classmethod
    def get_name(cls):
        if cls not in cls.registered_list:
            raise MyException(Exception)
        else:
            if hasattr(cls, '_name'):
                return cls._name
            else:
                return None

    @classmethod
    def register(cls):
        if cls.__name__ != "ClassFather":
            return cls.registered_list.append(cls)
        else:
            raise MyException(Exception)



class User1(ClassFather):
    _name = '1'


class User2(ClassFather):
    _name = '2'

