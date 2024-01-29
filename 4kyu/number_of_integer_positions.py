def partitions(number):
    def partitions_helper(number):
        answer = set()
        answer.add((number, ))
        for x in range(1, number):
            for y in partitions_helper(number - x):
                answer.add(tuple(sorted((x, ) + y)))

        return answer
    return len(partitions_helper(number))

print(partitions(25))