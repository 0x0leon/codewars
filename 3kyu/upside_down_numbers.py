import codewars_test as test

# nach wahrscheinlichkeiten schauen https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# 5 possibiliteis {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
'''


Calculating spinner count for 12345678900000000.
Range 1 - 9 has 3 spinners
Range 10 - 99 has 4 spinners
Range 100 - 999 has 12 spinners
Range 1000 - 9999 has 20 spinners
Range 10000 - 99999 has 60 spinners


Range 100000 - 999999 has 100 spinners
Range 1000000 - 9999999 has 300 spinners
Range 10000000 - 99999999 has 500 spinners
Range 100000000 - 999999999 has 1500 spinners
Range 1000000000 - 9999999999 has 2500 spinners
Range 10000000000 - 99999999999 has 7500 spinners
Range 100000000000 - 999999999999 has 12500 spinners
Range 1000000000000 - 9999999999999 has 37500 spinners
Range 10000000000000 - 99999999999999 has 62500 spinners
Range 100000000000000 - 999999999999999 has 187500 spinners
Range 1000000000000000 - 9999999999999999 has 312500 spinners

Subtotal of spinners from 1 to 16 digits: 624999

Range 10000000000000000 - 11999999999999999 has 93750 spinners.
1 1 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
1*2*5*5*5*5*5*5*3*1*1*1*1*1*1*1*1   -> 93750

Range 12000000000000000 - 12299999999999999 has 0 spinners.
Range 12300000000000000 - 12339999999999999 has 0 spinners.
Range 12340000000000000 - 12344999999999999 has 0 spinners.
Range 12345000000000000 - 12345599999999999 has 0 spinners.
Range 12345600000000000 - 12345669999999999 has 0 spinners.
Range 12345670000000000 - 12345677999999999 has 0 spinners.
Range 12345678000000000 - 12345678899999999 has 0 spinners.

Subtotal of spinners of 17 digits up to and including 12345678900000000: 93750
Total spinners: 718749
12345678900000000 has 718749 spinners.
Between 100000 - 12345678900000000 there are 718.650 spinners. 718.650


'''

spinners = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

asymmetric = ['0', '1', '8']
symmetric = ['6', '9']


def pblt(letter):
    '''return possibilities from letter '''
    return len([n for n in spinners if int(letter) <= int(n)])  # null


def detect_max_num(num):
    ''' return nearest lower num from wich is in spinners.keys '''
    nums = []
    for n in spinners.keys():
        if int(n) < int(num):
            nums.append(n)
    return nums[-1]


def check_if_spinner(num):
    '''check if number is spinnable'''
    for x in num:
        if x not in spinners.keys():
            return False
    return True


def count_digits(num):
    return len(num)


def generate_multiplies(x, y):
    return [10 ** x for x in range(len(x)-1, len(y))]


def upsidedown(x, y):
    """Count the number of upside-down numbers within the range [x, y]."""

    
    print(x, y)
    print(generate_multiplies(x, y))


@test.describe("Upside down numbers")
def upside_down_numbers():

    @test.it('Example Tests')
    def example_tests():
        test.assert_equals(upsidedown('0', '10'), 3)
        test.assert_equals(upsidedown('6', '25'), 2)
        test.assert_equals(upsidedown('10', '100'), 4)
        test.assert_equals(upsidedown('100', '1000'), 12)
        test.assert_equals(upsidedown('100000', '12345678900000000'), 718650)
