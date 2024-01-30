import codewars_test as test
import math


def circleIntersection():
    pass

@test.describe("Basic Tests")
def v():
    @test.it("It should works for basic tests.")
    def f():
        test.assert_equals(circleIntersection([0, 0], [7, 0], 5), 14)
        test.assert_equals(circleIntersection([0, 0], [0, 10], 10), 122)
        test.assert_equals(circleIntersection([5, 6], [5, 6], 3), 28)
        test.assert_equals(circleIntersection([-5, 0], [5, 0], 3), 0)
        test.assert_equals(circleIntersection([10, 20], [-5, -15], 20), 15)
        test.assert_equals(circleIntersection([-7, 13], [-25, -5], 17), 132)
        test.assert_equals(circleIntersection([-20, -4], [-40, 29], 7), 0)
        test.assert_equals(circleIntersection([38, -18], [46, -29], 10), 64)
        test.assert_equals(circleIntersection([-29, 33], [-8, 13], 15), 5)
        test.assert_equals(circleIntersection([-12, 20], [43, -49], 23), 0)
