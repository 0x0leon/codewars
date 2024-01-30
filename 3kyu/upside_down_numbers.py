import codewars_test as test

# nach wahrscheinlichkeiten schauen https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# 5 possibiliteis {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
'''

100 - 1000


self-spinning       0, 1, 8
pair-spinning       6, 9 - 9, 6


1000 - 10000

4 * 5 * 1 * 1 = 20

9000
3 * 5 * 1 * 1 = 15

10.000 - 100.000

4 * 5 * 5 * 1 * 1 * 1    = 100

900.000.000
3 * 5 * 5 * 5 * 3 * 1 * 1 * 1 * 1

1.000.000

4 * 5 * 5 * 3 * 1 * 1 * 1   = 300

900 000 000
4 * 5 * 5 * 5 * 3 * 1 * 1 * 1 * 1

8000000000

1 2 3 4 5 6 7 8 9 0 0 0 0 0 0 0 0
1 2 3 4 5 6 7 8 9 0 0 0 0 0 0 0 0
1*2*2*2*2*3*3*4*5*1*1*1*1*1*1*1*1


1 0 0 0 0 0
4*5*5*1*1*1                         -> 100

1 0 0 0 0 0 0
4*5*5*3*1*1*1                       -> 300

1 0 0 0 0 0 0 0
4*5*5*5*1*1*1*1                     -> 500

9 0 0 0 0 0 0 0 0
5*5*5*5*3*1*1*1*1                   -> 1875

1 0 0 0 0 0 0 0 0 0
4*5*5*5*5*1*1*1*1*1                 -> 2500

1 0 0 0 0 0 0 0 0 0 0
4*5*5*5*5*3*1*1*1*1*1               -> 7500

1 0 0 0 0 0 0 0 0 0 0 0
4*5*5*5*5*5*1*1*1*1*1*1             -> 12500

1 0 0 0 0 0 0 0 0 0 0 0 0
4*5*5*5*5*5*3*1*1*1*1*1*1           -> 37500

1 0 0 0 0 0 0 0 0 0 0 0 0 0
4*5*5*5*5*5*5*1*1*1*1*1*1*1         -> 62500

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
4*5*5*5*5*5*5*3*1*1*1*1*1*1*1       -> 187500

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0     -> 312500
4*5*5*5*5*5*5*5*1*1*1*1*1*1*1*1

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
Between 100000 - 12345678900000000 there are 718650 spinners.


'''

def upsidedown(x, y):
    """Count the number of upside-down numbers within the range [x, y]."""





@test.describe("Upside down numbers")
def upside_down_numbers():

    @test.it('Example Tests')
    def example_tests():
        test.assert_equals(upsidedown('0', '10'), 3)
        test.assert_equals(upsidedown('6', '25'), 2)
        test.assert_equals(upsidedown('10', '100'), 4)
        test.assert_equals(upsidedown('100', '1000'), 12)
        test.assert_equals(upsidedown('100000', '12345678900000000'), 718650)
