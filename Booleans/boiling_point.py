unit = input(
    'What unit are you using - \nf - Fahrenheit\nc - Celcius \nk - Kelvin? ')
temp = int(input("What temperature is the water? "))

if unit == 'f':
    if temp == 212:
        print('WHAT IS BOILING')
    else:
        print('WHAT IS NOT BOILING. MUST HIT 212F')
elif unit == 'c':
    if temp == 100:
        print('WHAT IS BOILING')
    else:
        print('WHAT IS NOT BOILING. MUST HIT 100C')
elif unit == 'k':
    if temp == 373:
        print('WHAT IS BOILING')
    else:
        print('WHAT IS NOT BOILING. MUST HIT 373K')
else:
    'The unit is not know'
    # f - 212
    # c - 100
    # k - 373
