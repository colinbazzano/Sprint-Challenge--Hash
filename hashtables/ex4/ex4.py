cache = {}


def has_negatives(a):
    for num in a:
        if num not in cache:
            cache[num] = num

        return cache[num]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
