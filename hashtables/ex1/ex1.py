cache = {}

weights_list = [4, 6, 10, 15, 16]
# , 5, 21


def get_indices_of_item_weights(weights, length, limit):
    for index, weight in enumerate(weights):
        cache[index] = weight
    for i in range(length):  # for the length of item weights
        value = weights[i]  # gets the values of the weights
        print("value:", value)
        key_to_find = limit - value
        print("key to find", key_to_find)
        if cache[value] is not None:
            print([cache[key_to_find], i])
            return ([cache[key_to_find], i])
        # if cache[key_to_find] is None:
        #     return
        #     print([cache[key_to_find], i])
        # return [cache[(cache, key_to_find), i]]

    return None


print(get_indices_of_item_weights(weights_list, 5, 21))

"""Criteria

input is a "package" with weights, length, and a (weight) limit.

finds TWO items, that the sum of them will be equal to the limit
if there isn't a sum that equals that, return NONE

Answer in a tuple format, with the larger value first (biggerItem, smallerItem)

"""
