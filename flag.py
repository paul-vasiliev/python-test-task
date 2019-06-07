# I wanted to have more flexible system. But maybe it is an overhead decision
class Conf:
    IN_SIGN = 'o'
    EX_SIGN = '*'
    BORDER = '#'
    WIDTH_COEF = 3
    HEIGHT_COEF = 2
    VERT_SPACE_COEF = 2


def flag(n):
    v = Validator(n)
    v.validate()

    border_line = Conf.BORDER * (Conf.WIDTH_COEF * n + 2)
    blank_lines = (
        f'{Conf.BORDER}{" " * Conf.WIDTH_COEF * n}{Conf.BORDER}'
        for _ in range(n // Conf.VERT_SPACE_COEF)
    )
    half_circle = []
    for i in range(n // 2):
        chord = f'{Conf.EX_SIGN}{Conf.IN_SIGN * i * 2}{Conf.EX_SIGN}'
        line = f'{Conf.BORDER}{chord:^{Conf.WIDTH_COEF * n}}{Conf.BORDER}'
        half_circle.append(line)
    half_flag = '\n'.join((border_line, *blank_lines, *half_circle))
    return '\n'.join((half_flag, half_flag[::-1]))


# I wanted to have various exception test for various validate errors
class Validator:
    validate_queue = ('type', 'pos', 'even')
    error_messages = {
        'type_error': 'Wrong datatype for n. '
                      'Please enter positive even number.',
        'pos_error': 'Entered number is less than zero. '
                     'Please enter positive even number.',
        'even_error': 'Entered number is not an even number. '
                      'Please enter positive even number',
    }

    def __init__(self, n):
        self.n = n

    def validate(self):
        for validate_type in self.validate_queue:
            if not getattr(self, f'{validate_type}_validate')():
                raise ArgumentError(
                    self.error_messages[f'{validate_type}_error']
                )

    def type_validate(self):
        return isinstance(self.n, int)

    def pos_validate(self):
        return self.n >= 0

    def even_validate(self):
        return not self.n % 2


class ArgumentError(Exception):
    pass


# This part was add only for selftesting
if __name__ == '__main__':
    assert flag(2) == '########\n' \
                      '#      #\n' \
                      '#  **  #\n' \
                      '#  **  #\n' \
                      '#      #\n' \
                      '########'
    assert flag(4) == '##############\n' \
                      '#            #\n' \
                      '#            #\n' \
                      '#     **     #\n' \
                      '#    *oo*    #\n' \
                      '#    *oo*    #\n' \
                      '#     **     #\n' \
                      '#            #\n' \
                      '#            #\n' \
                      '##############'
    assert flag(6) == '####################\n' \
                      '#                  #\n' \
                      '#                  #\n' \
                      '#                  #\n' \
                      '#        **        #\n' \
                      '#       *oo*       #\n' \
                      '#      *oooo*      #\n' \
                      '#      *oooo*      #\n' \
                      '#       *oo*       #\n' \
                      '#        **        #\n' \
                      '#                  #\n' \
                      '#                  #\n' \
                      '#                  #\n' \
                      '####################'
    assert flag(0) == '##\n' \
                      '##'
    try:
        flag('str')
    except ArgumentError as exp:
        print(exp)
    try:
        flag(5)
    except ArgumentError as exp:
        print(exp)
    try:
        flag(-2)
    except ArgumentError as exp:
        print(exp)
    print('ok')
