def extra_leter(a: str, b: str) -> str:
    leters = {}
    for el in a:
        if el in leters:
            leters[el] += 1
        else:
            leters[el] = 1

    for el in b:
        if el in leters:
            if leters[el] == 0:
                return el
            leters[el] -= 1
        else:
            return el
    return ''

print(extra_leter('uio', 'oeiu'))
print(extra_leter('fe', 'efo'))
print(extra_leter('ab', 'ab'))
print(extra_leter('bbb', 'bbbb'))