def day_1_a(entries):
    e_len = len(entries)
    for i in range(0, e_len):
        for j in range(e_len-1, -1, -1):
            if entries[i] + entries[j] == 2020:
                print(f"The solutions is {entries[i]} and {entries[j]} which multipled is {entries[i]*entries[j]}")
                return


def day_1_b(entries):
    e_len = len(entries)
    can = []
    for i in range(0, e_len):
        for j in range(e_len - 1, -1, -1):
            if entries[i] + entries[j] < 2020:
                can.append((i, j, entries[i] + entries[j]))

    c_len = len(can)
    for j in range(0, c_len):
        for i in range(e_len - 1, -1, -1):
            if entries[i] + can[j][2] == 2020:
                sol1 = can[j][0]
                sol2 = can[j][1]
                print(f"The solutions is {sol1} and {sol2} and {entries[i]} which multipled is {entries[sol1] * entries[sol2] * entries[i]}")
                return

if __name__ == '__main__':
    with open('input.txt','r') as input:
        lines = input.readlines()
        ee = [int(e) for e in lines]
    day_1_a(ee)
    day_1_b(ee)
