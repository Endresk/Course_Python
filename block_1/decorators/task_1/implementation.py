import time
from math import factorial


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args):
        st = time.time()
        fn = func(*args)
        return fn, f"Run time: {time.time() - st} sec."
    return wrapper


@time_execution
def fact(number):
    return factorial(number)


if __name__ == '__main__':
    num, time_ = fact(5)
    print(f"Factorial: {num} \n{time_}")