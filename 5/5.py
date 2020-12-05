def upper_half(s, e):
    return s+(round((e-s)/2)), e


def lower_half(s, e):
    return s, s+(round((e-s)/2))-1


def find_column(col_code, s=0, e=7):
    if len(col_code) == 1:
        if col_code[0] == 'L':
            return s
        else:
            return e
    if col_code[0] == 'L':
        return find_column(col_code[1:], *lower_half(s, e))
    else:
        return find_column(col_code[1:], *upper_half(s, e))


def find_row(row_code, s=0, e=127):
    if len(row_code) == 1:
        if row_code[0] == 'F':
            return s
        else:
            return e
    if row_code[0] == 'F':
        return find_row(row_code[1:], *lower_half(s, e))
    else:
        return find_row(row_code[1:], *upper_half(s, e))

scanned = []
def day_5_a(lines):
    highest_code = 0
    for line in lines:
        rows = line[:7]
        columns = line[7:]
        # print(find_row(rows))
        # print(find_column(columns))
        code = 8 * find_row(rows) + find_column(columns)
        scanned.append(code)
        print(f"R:{find_row(rows)},C:{find_column(columns)},code:{code}")
        if code >= highest_code:
            highest_code = code
    print(f"The highest code is: {highest_code}")


def possible_sits(rows=128,columns=8):
    ids = []
    for c in range(0, columns):
        for r in range(0, rows):
            ids.append(r*8+c)
    return ids


def day_5_b():
    not_found = set()
    ps = possible_sits()
    for p in ps:
        if p not in scanned:
            not_found.add(p)
    nf = sorted(list(not_found))
    j = 2
    res = []
    while j < len(nf):
        if nf[j-2] == nf[j-1] - 1 and nf[j] == nf[j-1] + 1:
            pass
        else:
            res.append(nf[j-1])
        j = j+1
    if len(res) == 3:
        print(f"The seat id is: {res[1]}")


if __name__ == '__main__':
    with open('input.txt','r') as fin:
        ll = fin.readlines()
    li = [lll.rstrip() for lll in ll]
    examples = ['FBFBBFFRLR', 'BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
    day_5_a(examples)
    day_5_a(li)
    day_5_b()