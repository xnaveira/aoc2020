def day_6_a(lines):
    answers = set()
    n_answers = []
    for ll in lines:
        if ll != '':
            for c in ll:
                answers.add(c)
        else:
            n_answers.append(len(answers))
            answers = set()
    sum_a = 0
    for a in n_answers:
        sum_a = sum_a + a
    print(f"The total number of answers is {sum_a}")


def intersect(l_sets):
    if len(l_sets) == 1:
        return l_sets[0]
    else:
        return l_sets[0].intersection(intersect(l_sets[1:]))


def day_6_b(lines):
    total_sum = 0
    l_sets = []
    for line in lines:
        if line != '':
            t_set = set()
            for c in line:
                t_set.add(c)
            l_sets.append(t_set)
        else:
            t_sum = len(intersect(l_sets))
            total_sum = total_sum + t_sum
            l_sets = []
    print(f"The sum of answers that everyone answered is: {total_sum}")


if __name__ == '__main__':
    with open('input.txt') as fin:
        li = fin.readlines()
        lin = [lll.rstrip() for lll in li]
    day_6_a(lin)
    day_6_b(lin)
