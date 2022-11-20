bottles = 99
while bottles > 0:
    print(f'{bottles} bottles of beer on the wall.')
    print(f'{bottles} bottles of beer.')
    if bottles == 1:
        print(
            f'Take one down, pass it around, no more bottles of beer on the wall.')
    else:
        print(
            f'Take one down, pass it around, {bottles-1} bottles of beer on the wall.')
    print('*' * 30)
    bottles -= 1
