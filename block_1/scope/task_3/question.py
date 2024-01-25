"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

"""

response:
3
3

nonlocal используется во вложенной функции и далее у нас переменная изменяется, 
соответственно number будет равен везде 3

"""