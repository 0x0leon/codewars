from itertools import product

nums = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '5', '6', '8', '4'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}


def get_pins(ob):
    return [''.join(x for x in i) for i in list(product(*[nums[x] for x in ob]))]


get_pins('369')
