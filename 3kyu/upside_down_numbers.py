import codewars_test as test


partners = [
    ['1', '1'],
    ['6', '9'],
    ['9', '6'],
    ['8', '8']
]


# nach wahrscheinlichkeiten schauen https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# 5 possibiliteis {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}


def upsidedown(a, b):
    nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    tot = 0
    for i in range(int(a), int(b)):
        i = str(i)
        m = "".join([nums[x] for x in i[::-1] if x in nums])
        if i == m:
            tot += 1
    return tot


@test.describe("Upside down numbers")
def upside_down_numbers():

    @test.it('Example Tests')
    def example_tests():
        test.assert_equals(upsidedown('0', '10'), 3)
        test.assert_equals(upsidedown('6', '25'), 2)
        test.assert_equals(upsidedown('10', '100'), 4)
        test.assert_equals(upsidedown('100', '1000'), 12)
        test.assert_equals(upsidedown('100000', '12345678900000000'), 718650)
