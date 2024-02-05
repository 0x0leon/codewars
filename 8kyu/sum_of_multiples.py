import codewars_test as test
import math


def sum_mul(n, m):
    return sum(i for i in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'



@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Predefined tests')
    def basic_test_cases():
        test.assert_equals(sum_mul(0, 0), 'INVALID')
        test.assert_equals(sum_mul(2, 9), 20)
        test.assert_equals(sum_mul(4, -7), 'INVALID')
        test.assert_equals(sum_mul(4, 123), 1860)
        test.assert_equals(sum_mul(123, 4567), 86469)

    @test.it('Should not include m')
    def basic_test_cases():
        test.assert_equals(sum_mul(2, 10), 20)

    @test.it('Should work for n == m')
    def basic_test_cases():
        test.assert_equals(sum_mul(2, 2), 0)
        test.assert_equals(sum_mul(7, 7), 0)

    @test.it('Should work for n > m')
    def basic_test_cases():
        test.assert_equals(sum_mul(7, 2), 0)
        test.assert_equals(sum_mul(21, 3), 0)

    @test.it('Zero is not a natural number (for this kata at least)')
    def basic_test_cases():
        test.assert_equals(sum_mul(0, 2), 'INVALID')
        test.assert_equals(sum_mul(2, 0), 'INVALID')

    @test.it('Negative numbers')
    def basic_test_cases():
        test.assert_equals(sum_mul(4, -7), 'INVALID')
        test.assert_equals(sum_mul(-7, 4), 'INVALID')
