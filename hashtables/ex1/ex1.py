

weights_list = [4, 6, 10, 15, 16]
# , 5, 21


def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    duplicates = False
    duplicates_dict = {}

    for i in range(length):  # for the length of item weights
        value = weights[i]  # gets the values of the weights
        cache[value] = i
        key_to_find = limit - value
        if key_to_find in cache:
            if value > key_to_find:
                return (i, cache[key_to_find])
            elif value < key_to_find:
                return (i, cache[key_to_find])
            elif key_to_find == value:
                if duplicates is False:
                    duplicates = True
                    duplicates_dict[value] = i
                elif duplicates is True:
                    return (i, duplicates_dict[value])

    return None


"""Criteria

input is a "package" with weights, length, and a (weight) limit.

finds TWO items, that the sum of them will be equal to the limit
if there isn't a sum that equals that, return NONE

Answer in a tuple format, with the larger value first (biggerItem, smallerItem)

"""
