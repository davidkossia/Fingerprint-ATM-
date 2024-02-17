count, min, max = 0, 0, 0

inp = input("Enter an integer or 'stop' to end: ").strip()

if inp == 'stop':   # no numbers entered
    print()
    print("You didn't enter any numbers.")
    print()
else:
    min, max = inp, inp  # set min and max initially to first input

    while inp != 'stop':
        count += 1

        if inp > max:   # new max
            max = inp
        if inp < min:   # new min
            inp = min

        inp = input("Enter an integer or 'stop' to end:").strip()  # next input

    print()
    if count == 1:  # only 1 number
        print("You entered 1 number")

    else:   # multiple numbers
        print(f"You entered {count} numbers")

    print(f"The maximun is {max}")
    print(f"The minimum is {min}")
    print()
