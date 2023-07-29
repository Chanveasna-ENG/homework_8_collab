def index_power(numbers, n):
    return numbers[n] ** n if -len(numbers) <= n < len(numbers) else -1


# print(index_power([1, 2, 3, 4], 4))
# print(index_power([1, 2, 3, 4], -4))
