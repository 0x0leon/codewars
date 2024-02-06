import codewars_test as test


def upsidedown(lower_bound, upper_bound):
    valid_pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    memo = {}

    def helper(n, is_limit, prefix, suffix):
        if n == 0:
            return 1 if not is_limit or prefix + suffix <= upper_bound else 0
        if n == 1:
            count = 0
            for digit in '018':
                if not is_limit or prefix + digit + suffix <= upper_bound:
                    count += 1
            return count
        if (n, is_limit) in memo and not is_limit:
            return memo[(n, is_limit)]

        count = 0
        for a, b in valid_pairs:
            if n != len(lower_bound) or a != '0':  # Avoid leading zero
                new_prefix = a + prefix
                new_suffix = suffix + b
                if not is_limit or new_prefix + ('0' * (n - 2)) + new_suffix <= upper_bound:
                    count += helper(n - 2, is_limit and new_prefix + ('9' * (n - 2)) +
                                    new_suffix >= lower_bound, new_prefix, new_suffix)

        if not is_limit:
            memo[(n, is_limit)] = count
        return count

    total_count = sum(helper(n, True, '', '')
                      for n in range(len(lower_bound), len(upper_bound) + 1))
    return total_count


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
