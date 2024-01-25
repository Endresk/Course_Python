def counter():
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrapper():
        wrapper.calls += 1
        return wrapper.calls

    wrapper.calls = 0

    return wrapper

