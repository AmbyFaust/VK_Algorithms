def annograms(words: list[str]) -> list[list[str]]:
    res = []
    if len(words) == 0:
        return res
    words_sorted = [[''.join(sorted(list(words[i].lower()))), i] for i in range(len(words))]
    words_sorted.sort(key=lambda x: x[0])
    base = words_sorted[0][0]
    tmp = []
    for el in words_sorted:
        if el[0] != base:
            base = el[0]
            res.append(tmp)
            tmp = []
        tmp.append(words[el[1]])
    res.append(tmp)
    return res
