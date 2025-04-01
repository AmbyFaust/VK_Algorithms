def animal_and_food(animals: list, food: list):
    if not animals or not food:
        return 0
    animals.sort()
    food.sort()
    f = len(food) - 1
    a = len(animals) - 1
    res = 0
    while f and a:
        if animals[f] > food[a]:
            a -= 1
        else:
            f -= 1
            res += 1
    return res

