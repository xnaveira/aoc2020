import re

valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional = ['cid']
valid1_r = []

def process_fields(fields):
    if len(fields.split(' ')) < 7:
        return 0
    for v in valid:
        if not re.search(v+':', fields):
            return 0
    return 1


def day_4_a(lines):
    fields = ""
    n_valid = 0
    for lll in lines:
        if lll != "":
            fields = fields + ' ' + lll
        else:
            if process_fields(fields.strip()) == 1:
                valid1_r.append(fields.strip())
            n_valid = n_valid + process_fields(fields.strip())
            fields = ""
    print(f"The number of valid passports is {n_valid}")


def check_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False

def check_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False

def check_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False

def check_hgt(hgt):
    is_cm = hgt.split('cm')
    is_in = hgt.split('in')
    if len(is_cm) > 1:
        if 150 <= int(is_cm[0]) <= 193:
            return True
    if len(is_in) > 1:
        if 59 <= int(is_in[0]) <= 76:
            return True
    return False

def check_hcl(hcl):
    v = hcl.split('#')
    if len(v) > 1 and v[0] == '':
        if len(v[1]) == 6:
            return True
    return False

def check_ecl(ecl):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in valid_ecl:
        return True
    else:
        return False

def check_pid(pid):
    if len(pid) == 9:
        return True
    else:
        return False


def day_4_b():
    super_valid = 0
    vv = True
    for lll in valid1_r:
        fields = lll.split(' ')
        for f in fields:
            if 'pid' in f:
                if not check_pid(f.split(':')[1]):
                    vv = False
            if 'ecl' in f:
                if not check_ecl(f.split(':')[1]):
                    vv = False
            if 'hcl' in f:
                if not check_hcl(f.split(':')[1]):
                    vv = False
            if 'hgt' in f:
                if not check_hgt(f.split(':')[1]):
                    vv = False
            if 'eyr' in f:
                if not check_eyr(f.split(':')[1]):
                    vv = False
            if 'iyr' in f:
                if not check_iyr(f.split(':')[1]):
                    vv = False
            if 'byr' in f:
                if not check_byr(f.split(':')[1]):
                    vv = False
        if vv:
            super_valid = super_valid + 1
        else:
            vv = True
    print(f'The number of super valid passports is {super_valid}')


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        lin = fin.readlines()
        lins = [ll.rstrip() for ll in lin]
    day_4_a(lins)
    day_4_b()
