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

        100000
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


        10000000000000000
        11999999999999999
Range   10000000000000000 - 11999999999999999 has 93750 spinners.
1 1 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
1*2*5*5*5*5*5*5*3*1*1*1*1*1*1*1*1   -> 93750
1 2 3 4 5 6 7 8 9 0 0 0 0 0 0 0 0


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










1 2 1 6 7 2

1*2*1*1*1*1
















'''

spinners = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

asymmetric = ['0', '1', '8']
symmetric = ['6', '9']


def pblt(letter):
    '''return possibilities from letter '''
    return len([n for n in spinners.keys() if int(letter) <= int(n)])  # null


def check_if_spinner(num):
    '''check if number is spinnable'''
    for x in num:
        if x not in spinners.keys():
            return False
    return True


def calc_pblt_to_ten(char):
    return len([n for n in spinners.keys() if int(char) <= int(n)])  # null


def calc_pblt_to_ten_single(char):
    # null
    return len([n for n in spinners.keys() if int(char) <= int(n) and n not in symmetric])


def is_even(num):
    if len(num) % 2 == 0:
        return True


def calc_pblt_to_ten_list(lst):
    pblt = 1
    # print(f'calc_pblt_to_ten_list({lst})')
    if len(lst) == 1:
        return calc_pblt_to_ten_single(lst)

    elif is_even(lst):
        for num in lst[:len(lst) // 2]:
            pblt *= calc_pblt_to_ten(num)
    else:
        for num in lst[:len(lst) // 2]:
            pblt *= calc_pblt_to_ten(num)
        pblt *= 3

    return pblt


def calc_pblt_in_range(start, end):
    return len([n for n in spinners.keys() if int(start) <= int(n) <= int(end)])


def calc_pblt_in_range_list(start, end):
    pblt = []
    c = 0
    for x in start:
        pblt.append(calc_pblt_in_range(x, end[c]))
        c += 1
    if len(pblt) % 2 == 0:
        return calc_pblt(pblt[:len(pblt) // 2])
        # handle gerade anzahl

    elif len(pblt) % 2 != 0:
        tmp = pblt[:(len(pblt)-1) // 2]
        tmp.append(3)
        return calc_pblt(tmp)
        # handle ungerade


def calc_pblt_to_specific(num):
    return len([n for n in spinners.keys() if int(n) <= int(num)])  # null


def calc_pblt_to_specific_list(lst):
    pblt = []
    c = 0
    n_x = generate_nearest_x(lst)
    for x in n_x:
        pblt.append(calc_pblt_to_specific(x))
        # print("calc_pblt_range: ", x, end[c], calc_pblt_in_range(x, end[c]))
        c += 1

    if len(pblt) % 2 == 0:
        return calc_pblt(pblt[:len(pblt) // 2])
        # handle gerade anzahl

    elif len(pblt) % 2 != 0:
        return calc_pblt(pblt[:(len(pblt)-1) // 2])
        # handle ungerade


def generate_nearest_x(x):
    return '1' + (len(x) * '0')


def generate_nearest_y(y):
    return '1' + ((len(y)-1) * '0')


def x_to_tenth(x):
    nearest = str(10 ** len(x))
    pblts = []

    '''
    case x = 4
    nearest = 10 ^ 1

    '''

    calc_pblt_to_specific(nearest)

    # print(f'log__x_to_tenth, x::{x} nearest::{nearest}, pblts::{pblts}')
    return nearest, pblts


def tenth_to_tenth(xtt, tty):
    ''' generate string from xtt(ex. 10) to tty (ex. 100000)'''
    nums = []
    # 10 ^ 1
    xt = '1' + ((len(xtt)-1) * '0')
    nums.append(xt)

    for i in range(len(xtt), len(tty)):
        xt += '0'
        nums.append(xt)

    return nums


def calc_pblt(nums):
    i = 1
    for n in nums:
        i *= n
    return i


def calc_pblts(nums):
    ''' calculate possiblties'''

    if len(nums) == 1:
        return nums
    elif len(nums) % 2 == 0:
        return calc_pblt(nums[:len(nums) // 2])
        # handle gerade anzahl

    elif len(nums) % 2 != 0:
        return calc_pblt(nums[:(len(nums)-1) // 2])
        # handle ungerade


def find_lower_matching_for_y(y):
    better_string = ""
    ind = 0
    for i in range(len(y)):

        if y[i] not in spinners.keys():
            ind = i
            better_string += [x for x in spinners.keys()
                              if int(x) <= int(y[i])][-1]
            break

        better_string += y[i]

    better_string += ((len(y)-1) - ind) * '9'

    return better_string


def upsidedown(x, y):
    """Count the number of upside-down numbers within the range [x, y]."""

    print(f'x {x}, y {y}')
    # print(calc_pblt_to_ten_list(x))

    '''
    1 0 0 0 0
    4*5*3*1*1 = 60


    '''

    if len(x) == 1 == len(y):
        return calc_pblt_in_range(x, y)

    nearest_for_x = generate_nearest_x(x)
    nearest_for_y = generate_nearest_y(y)

    nums = tenth_to_tenth(nearest_for_x, nearest_for_y)

    if len(nums) == 1:
        pblt_x = calc_pblt_to_ten_list(nums[0])

        if nums[0] == y:
            return calc_pblt_to_ten_list(x)
        else:

            pblt_x = calc_pblt_to_ten_list(x)
            pblt_y = calc_pblt_in_range_list(nearest_for_x, y)
            return pblt_x + pblt_y
    else:

        pblt_ = 0
        pblt_ += calc_pblt_in_range_list(x, nearest_for_x)
        print("1---> ", pblt_)
        for c in nums[0:-1]:
            pblt_ += calc_pblt_to_ten_list(c)
            print(calc_pblt_to_ten_list(c))

        pblt_ += calc_pblt_in_range_list(nearest_for_y,
                                         find_lower_matching_for_y(y))

        print(find_lower_matching_for_y('7208680089150825'))

        return pblt_


@test.describe("Upside down numbers")
def upside_down_numbers():

    @test.it('Example Tests')
    def example_tests():
        test.assert_equals(upsidedown('0', '10'), 3)
        test.assert_equals(upsidedown('6', '25'), 2)
        test.assert_equals(upsidedown('10', '100'), 4)
        test.assert_equals(upsidedown('100', '1000'), 12)
        test.assert_equals(upsidedown('100000', '12345678900000000'), 718650)
        test.assert_equals(upsidedown('6212', '38823686'), 598)
        test.assert_equals(upsidedown('1926', '3038129'), 251)
        test.assert_equals(upsidedown('75', '682856'), 136)
        test.assert_equals(upsidedown('2327', '30054320'), 600)
        test.assert_equals(upsidedown('4133', '121672'), 85)
        test.assert_equals(upsidedown('64', '88954'), 77)

        test.assert_equals(upsidedown('378526', '2429854'), 150)
        test.assert_equals(upsidedown(
            '93440695', '431312852394405329234040985591'), 30517577200)
        test.assert_equals(upsidedown(
            '98111190106111186', '695543100659359251322361425761937994953893'), 560760496566364)
        test.assert_equals(upsidedown(
            '3559370613066', '38409974515928025704202956388850491169'), 19073486293750)


'''

Range 1 - 9 has                 3 spinners
Range 10 - 99 has                4 spinners
Range 100 - 999 has             12 spinners
Range 1000 - 9999 has           20 spinners
Range 10000 - 99999 has             60 spinners

        100000
Range 100000 - 999999 has       100 spinners
Range 1000000 - 9999999 has     300 spinners
..                              = 500
..                              = 1.500
..                              = 2.500
..                              = 7.500
..                              = 12.500
..                              = 37.500

..                                = 62.500

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 = 187.500

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3*5*5*5*5*5*5*5*1*1*1*1*1*1*1*1 = 234.375
6 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 

7 2 0 8 6 8 0 0 8 9 1 5 0 8 2 5
3*2*1*4*3*4*1*1*1*1*1*1*1*1*1*1 = 288

                                                    468.625









'''
