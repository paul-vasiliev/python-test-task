import argparse


def check(num):
    try:
        num = int(num)
        if num > 0 and num % 2 == 0:
            return True
    except Exception:
        return False


def flag(num):
    up_half = '#'*(3*num+2) + '\n'
    for line in range(num):
        if line < num // 2:
            up_left_part = '#' + ' ' * (3 * (num // 2))
        else:
            up_left_part = '#' + ' ' * (2*num - line - 1) + '*' + 'o'*(line - num//2)
        up_half += up_left_part + up_left_part[::-1] + '\n'
    all_flag = up_half[:-1] + up_half[::-1]
    return all_flag


def main():
    parser = argparse.ArgumentParser(description='Takes number')
    parser.add_argument('number', help='N must be a valid even number', default=0)
    number = parser.parse_args().number
    if check(number):
        print(flag(int(number)))
    else:
        print('N must be a valid even number')


if __name__ == '__main__':
    main()
