import codewars_test as test


spinners = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


def find_nearest_spinner_num():

    pass


def get_pblt(x, y):

    pblt = []

    pblt.append(x)

    n_x = x
    for i in range(len(x), len(y)):
        n_x += '0'

        print(n_x)


def upsidedown(x, y):

    

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
