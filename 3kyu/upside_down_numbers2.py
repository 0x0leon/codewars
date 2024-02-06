import codewars_test as test


class Solution:
    def upsidedown(self, low: str, high: str) -> int:
        # Helper function to generate strobogrammatic numbers of length 'length'
        def generate_strobogrammatic(length):
            # Base case for a strobogrammatic number of length 0 is an empty string
            if length == 0:
                return ['']
            # Base case for length 1 (single digit strobogrammatic numbers)
            if length == 1:
                return ['0', '1', '8']
            sub_ans = []
            # Recursive call to get the inner strobogrammatic number
            for sub_number in generate_strobogrammatic(length - 2):
                # Adding the strobogrammatic pairs to the sub_number
                for pair in ('11', '88', '69', '96'):
                    sub_ans.append(pair[0] + sub_number + pair[1])
                # Numbers like '060', '080' etc. cannot be at the beginning or end
                # So we add them only when we're not at the outermost level
                if length != num_length:
                    sub_ans.append('0' + sub_number + '0')
            return sub_ans

        min_length, max_length = len(low), len(high)
        low, high = int(low), int(high)
        count = 0  # Counter for strobogrammatic numbers within the range

        # Loop through all lengths from min_length to max_length
        for num_length in range(min_length, max_length + 1):
            # generate strobogrammatic numbers of length 'num_length'
            for num_str in generate_strobogrammatic(num_length):
                # Convert the string to an integer and check if it's within range
                if low <= int(num_str) <= high:
                    count += 1
        return count  # Return the count of strobogrammatic numbers within the range


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
