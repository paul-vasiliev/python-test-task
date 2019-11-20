import argparse


class Settings:
    flag_border_symbol = '#'
    canvas_symbol = ' '
    circle_border_symbol = '*'
    circle_symbol = 'o'


def verification(func):
    def wrapper(n):
        if not isinstance(n, int):
            raise argparse.ArgumentError(None, f'{type(n)} "{n}" has an invalid data type.')
        if n < 0:
            raise argparse.ArgumentError(None, f'{type(n)} "{n}" must be greater than 0.')
        if n % 2 != 0:
            raise argparse.ArgumentError(None, f'{type(n)} "{n}" should be even.')
        return func(n)

    return wrapper


@verification
def flag(n):
    half_n = n // 2
    half_flag = Settings.flag_border_symbol * (3*n + 2) + '\n'
    for num_line in range(2 * half_n):
        half_line = Settings.flag_border_symbol + \
               (Settings.canvas_symbol * (3 * half_n) if num_line < half_n
                else Settings.canvas_symbol * (2 * n - num_line - 1) + Settings.circle_border_symbol +
                Settings.circle_symbol * (num_line - half_n))
        half_flag += half_line + half_line[::-1] + '\n'
    full_flag = half_flag[:-1] + half_flag[::-1]
    return full_flag


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Takes the value n')
    parser.add_argument('n', type=int, help='n must be a valid even number.', default=0)
    n = parser.parse_args().n
    print(flag(n))
