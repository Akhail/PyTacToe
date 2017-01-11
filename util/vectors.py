import random


def find_random(vec, num):
    o = random.randint(0, vec.count(num) - 1)
    c = 0

    for idx, val in enumerate(vec):
        if val == num:
            if c == o:
                return idx
            c += 1
