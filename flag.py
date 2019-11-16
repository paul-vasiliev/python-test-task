class Settings:
    flag_border_symbol = '#'
    canvas_symbol = ' '
    circle_border_symbol = '*'
    circle_symbol = 'o'


def flag(n):
    verification(n)

    half_n = n // 2
    half_width = 3 * half_n
    half_height = 2 * half_n

    half_flag = str()
    for num_line in range(half_height + 1):  # the flag is symmetrical horizontally, so we will generate half of it
        half_flag += get_line(num_line, half_n, half_width, half_height)
    full_flag = half_flag[:-1] + half_flag[::-1]  # add half and its mirror image
    return full_flag


def get_line(num_line, half_n, half_width, half_height):
    half_line = Settings.flag_border_symbol
    if num_line > half_n:  # case when part of the circle must be present
        half_line += get_half_line_1(num_line, half_n)
    elif num_line > 0:
        half_line += Settings.canvas_symbol * half_width
    else:
        half_line += Settings.flag_border_symbol * half_width
    line = half_line + half_line[::-1] + '\n'
    return line


def get_half_line_1(num_line, half_n):
    # generation as shown in the examples

    half_line = Settings.canvas_symbol * (4 * half_n - num_line) + Settings.circle_border_symbol + \
                Settings.circle_symbol * (num_line - half_n - 1)
    return half_line


def get_half_line_2(num_line, half_n, half_width, half_height):
    # generation according to the formula for a circle (the circle should not be a rhombus)

    start_circle_x = int(half_width + 0.5 - (half_n ** 2 - (num_line - (half_height + 0.5)) ** 2) ** 0.5)
    half_line = Settings.canvas_symbol * start_circle_x + Settings.circle_border_symbol + \
                Settings.circle_symbol * (half_width - start_circle_x - 1)
    return half_line


class ArgumentError(Exception):
    pass


def verification(n):
    try:
        if not isinstance(n, int):
            raise ArgumentError(f'{type(n)} "{n}" has an invalid data type.')
        if n < 0:
            raise ArgumentError(f'{type(n)} "{n}" must be greater than 0.')
        if n % 2 != 0:
            raise ArgumentError(f'{type(n)} "{n}" should be even.')
    except ArgumentError as exc:
        print(f'{exc}\n"N" must be a valid even number.')
        raise


if __name__ == '__main__':
    print(flag(8))
