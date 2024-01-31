
class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args):
        self.items = tuple(args)

    def __getitem__(self, index):
        return self.items[index]

    def __delitem__(self, index):
        raise TypeError

    def __setitem__(self, index):
        raise TypeError

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        return self.items.count(value)

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        return self.items.index(value)
