"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


"""

response:
Test message
None

В функции сначала вызывается другая функция "data_transmitter()", которая выводит ""Test message"", функция завершается
и возврашаемого результата нет, соответственно по умолчанию он ""None""

"""