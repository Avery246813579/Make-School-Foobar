"""
You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.
While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British pounds
For example:

  # weighs 7 kilograms and has a value of 160 pounds
(7, 160)

# weighs 3 kilograms and has a value of 90 pounds
(3, 90)

You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

For example:

  cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)

Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our algorithms flexible and comprehensive.
"""


def answer(types, bag_weight):
    ratio = []

    for weight, value in types:
        vw_ratio = float(value) / weight
        ratio.append((vw_ratio, (weight, value)))

    total = 0
    while len(ratio) > 0:
        b_r = ratio[0]
        b_i = 0

        for i in range(1, len(ratio)):
            c_ratio = ratio[i]

            if c_ratio[0] > b_r[0]:
                b_r = c_ratio
                b_i = i
            elif c_ratio[0] == b_r[0] and c_ratio[1][1] < b_r[1][1]:
                b_r = c_ratio
                b_i = i

        del ratio[b_i]

        usages = bag_weight // b_r[1][0]
        total += usages * b_r[1][1]
        bag_weight -= usages * b_r[1][0]

        if bag_weight == 0:
            break

    return total


def answer2(types, bag_weight):
    total = 0
    while len(types) > 0:
        b_r = types[0]
        b_i = 0

        for i in range(1, len(types)):
            weight, value = types[i]

            if value / weight > b_r[1] / b_r[0]:
                b_r = types[i]
                b_i = i
            elif value / weight == b_r[1] / b_r[0] and weight < b_r[0]:
                b_r = types[i]
                b_i = i

        del types[b_i]

        usages = bag_weight // b_r[0]
        total += usages * b_r[1]
        bag_weight -= usages * b_r[0]

        if bag_weight == 0:
            break

    return total


print(answer2([(7, 160), (3, 90), (2, 15)], 20))
