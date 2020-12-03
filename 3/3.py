def day_3_a(lines, right=3, down=1):
    num_lines = len(lines)
    num_col = num_lines * right
    num_blo = int((num_col / 10) + 1)
    mapt = [line * num_blo for line in lines]
    x = 0
    y = 0
    trees = 0
    for line in mapt:
        if y % down == 0:
            if line[x] == '#':
                trees = trees + 1
            x = x + right
        y = y + 1
    print(f"The total number of encountered trees is: {trees}")
    return trees


def day_3_b(lines):
    route1 = day_3_a(lines, 1, 1)
    route2 = day_3_a(lines, 3, 1)
    route3 = day_3_a(lines, 5, 1)
    route4 = day_3_a(lines, 7, 1)
    route5 = day_3_a(lines, 1, 2)

    print(f"The total number of multiplied trees is: {route1 * route2 * route3 * route4 * route5}")


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        li = fin.readlines()
        listripped = [l.rstrip() for l in li]
        day_3_a(listripped)
        day_3_b(listripped)
