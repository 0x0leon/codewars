import codewars_test as test


def happy(i):
    j = 0
    while (i != 0):
        j += (i % 10)*(i % 10)
        i -= (i % 10)
        i /= 10

    return j

def is_happy(i):
    if i == 1:
        return True
    elif i == 4:
        return False
    else:
        return is_happy(happy(i))


def perf_happy(n):
    j = []
    for i in range(1, n+1):
        if is_happy(i):
            j.append(i)
    return j

@test.describe("Sample tests")
def _():
    @test.it("Fixed tests")
    def _():
        test.assert_equals(perf_happy(100), [
                           1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100])
        test.assert_equals(perf_happy(999), [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446,
                           464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998])