import codewars_test as test


def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce < 0 or bounce >= 1 or window > h:
        return -1

    count = 1
    bouncing = h * bounce
    while bouncing > window:

        bouncing *= bounce
        count += 2

    return count

@test.describe('Tests')
def fixed_tests():
    def testing(h, bounce, window, exp):
        actual = bouncing_ball(h, bounce, window)
        test.assert_equals(actual, exp)

    @test.it('Fixed Tests')
    def tests():
        testing(2, 0.5, 1, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)
