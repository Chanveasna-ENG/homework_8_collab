def chunking_by(numbers, chunk):
    new = []

    if chunk == 0:
        return numbers

    while len(numbers) / chunk >= 1:
        new.append(numbers[0:chunk])
        del numbers[0:chunk]
    if len(numbers) > 0:
        new.append(numbers)
    return new
