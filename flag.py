from argparse import ArgumentError


def flag(n):
    REC_BORDER = '#'
    CIRC_BORDER = '*'
    IN_SIGN = 'o'
    WIDTH = 3
    HEIGHT = 2
    border_line = REC_BORDER * ( WIDTH * n + 2)
    blank_line = REC_BORDER + WIDTH * " " * n + REC_BORDER 
    half_flag = []
    half_flag.append(border_line)
    for i in range(n//2):
        half_flag.append(blank_line)
    for i in range(n//2):
        flag_chunk = CIRC_BORDER + i*IN_SIGN*2+CIRC_BORDER
        line = REC_BORDER +\
               " " * n +\
               " "  * ((n - (2 * i)) // 2 - 1) +\
               flag_chunk +\
               " " * ((n - (2 * i)) // 2 - 1) +\
               " " * n +\
               REC_BORDER
        half_flag.append(line)
    res = '\n'.join(half_flag)
    return '\n'.join([res, res[::-1]])



N = input("Введите число: ")
if N.isdigit() and int(N)%2==0:
    N = int(N)
    print(flag(N))
else:
    raise ArgumentError(None, "Не является натуральным чётным числом.")
