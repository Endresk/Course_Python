def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """

    return 1.8 * int(value) + 32 if to_scale == 'F' else 5/9 * (int(value) - 32) if to_scale == 'C' else value

