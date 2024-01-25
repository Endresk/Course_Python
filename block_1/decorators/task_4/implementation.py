import time

from block_1.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator(func):

        def wrapper():
            count = 0
            while count < times:
                try:
                    result = func()
                    if result is not None:
                        return result
                except AssertionError:
                    count += 1
                time.sleep(delay)
            raise MyException(Exception)
        return wrapper
    return decorator

