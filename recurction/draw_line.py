def drow_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def drow_interval(center_length):
    if center_length > 0:
        drow_interval(center_length - 1)
        drow_line(center_length)
        drow_interval(center_length - 1)


def drow_rules(num_inches, major_length):
    drow_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        drow_interval(major_length - 1)
        drow_line(major_length, str(j))


if __name__ == "__main__":
    drow_rules(3, 4)