def two_sum(a: list, target: int) -> list[int]:
    digits = {}
    for el in a:
        if el in digits:
            digits[el] += 1
        else:
            digits[el] = 1

    for key in digits:
        digits[key] -= 1
        if target - key in digits and digits[target - key]:
            return [key, target - key]
    return []


print(two_sum([1, 2, 3, 4, 5], 0))
