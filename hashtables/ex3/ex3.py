from collections import defaultdict


def intersection(arrays):
    cache = defaultdict(int)  # needed a default dict to avoid KeyError

    for array in arrays:
        for number in array:
            cache[number] += 1
    result = [i for i in cache if cache[i] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
