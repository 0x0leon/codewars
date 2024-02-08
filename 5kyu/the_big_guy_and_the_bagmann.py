import codewars_test as test


def best_route(cities, costs):
    sol = []
    l = {i: x for i, x in enumerate(zip(cities, costs))}

    start = 0
    # print(start)

    def helper(index):
        vals = l[index][1]
        if l[index][0] == "Notgnihsaw":
            return
        
        target = min([i for i in vals if i != 0])
        ind = vals.index(target)

        sol.append(l[ind][0])
        print(index)

        return helper(ind)

    helper(start)
    print(sol)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(best_route(['Notgnihsaw', 'Berlin', 'Helsinki'],
                                      [[0, 800, 1500], [900, 0, 350], [1200, 650, 0]]),
                           ['Berlin', 'Helsinki', 'Notgnihsaw'])
        test.assert_equals(best_route(['Aleppo', 'Shenyang', 'Notgnihsaw', 'Vienna', 'Buenos Aires'],
                                      [[0, 1800, 1250, 1500, 2450],
                                       [1400, 0, 1900, 1150, 2000],
                                       [1300, 1200, 0, 900, 1450],
                                       [3000, 1950, 800, 0, 1700],
                                       [2800, 2400, 1650, 2250, 0]]),
                           ['Shenyang', 'Aleppo', 'Vienna', 'Buenos Aires', 'Notgnihsaw'])
