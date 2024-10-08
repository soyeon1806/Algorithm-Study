def solution(N, number):

    if number == 1:
        return 1
    set_list = []

    for answer in range(1, 9):
        partial_set = set()
        partial_set.add(int(str(N) * answer))
        for i in range(answer - 1):
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)

                    if op2 != 0:
                        partial_set.add(op1 / op2)

        if number in partial_set:
            return answer
        set_list.append(partial_set)

    return -1