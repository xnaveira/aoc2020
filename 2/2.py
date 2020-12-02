
def day_2_a(pp):
    valid = 0
    for p in pp:
        rule = p[0]
        password = p[1]
        c = rule.split()[1]
        minc = int(rule.split()[0].split('-')[0])
        maxc = int(rule.split()[0].split('-')[1])
        if maxc >= password.count(c) >= minc:
            valid = valid + 1
    print(f'The number of valid passwords according to policy 1 is: {valid}')


def day_2_b(pp):
    valid = 0
    for p in pp:
        rule = p[0]
        password = p[1]
        c = rule.split()[1]
        minc = int(rule.split()[0].split('-')[0])
        maxc = int(rule.split()[0].split('-')[1])
        if password[minc] == c:
            if password[maxc] != c:
                valid = valid + 1
        else:
            if password[maxc] == c:
                valid = valid + 1
    print(f'The number of valid passwords according to policy 2 is: {valid}')


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        lines = fin.readlines()
        ppp = [(line.split(':')[0],line.split(':')[1]) for line in lines ]
        day_2_a(ppp)
        day_2_b(ppp)