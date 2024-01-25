from block_1.common import MyException


def check_value(fact):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(num):
        if isinstance(num, int) and num >= 0:
            return fact(num)
        else:
            raise MyException(Exception)

    return wrapper