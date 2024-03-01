def fib(num):
    fib1, fib2, series = 0, 1, 0

    for x in range(num):
        fib1 = fib2
        fib2 = series
        series = fib1 + fib2

        yield series