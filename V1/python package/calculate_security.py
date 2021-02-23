def calculate_security(key="mCypt", hashespersec=1000000):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    key_list = []
    key_list += key

    checklist = [False, False, False, False]
    for letter in key_list:
        # Checks Spelling
        if letter in lower:
            checklist[0] = True
        if letter in upper:
            checklist[1] = True
        if letter in numbers:
            checklist[2] = True

        if letter not in lower or \
           letter not in upper or \
           letter not in numbers:
            checklist[3] = True

    maths_stuff = 0
    if checklist[0]:
        maths_stuff += 26
    if checklist[1]:
        maths_stuff += 26
    if checklist[2]:
        maths_stuff += 10
    if checklist[3]:
        maths_stuff += 20

    combinations = maths_stuff**len(key)

    time2crack = round(combinations / hashespersec)

    return [combinations, time2crack]
