def fibonacci(max_number):
    start, next = 0, 1
    serie = []

    for _ in range(max_number):
        serie.append( start + next )

        start, next = next, serie[-1]

    return serie