def scramble_str(
        key="mCrypt",
        data="Lorem ipsum dolor sit amet,",
        motd=False,
        large_str=False
        ):
    from math import floor

    if motd:
        from time import process_time
        timer = process_time()

    # how often key fits in
    fits = floor(len(data) / len(key))
    total = len(data) - (len(key) * fits)

    if not large_str:
        # make long enough key
        key_adapted = ''
        for i in range(0, fits):
            key_adapted += key
        key_adapted += key[0:total]
    else:
        # Very complext (JK)
        # list of number of "fits in"
        list_fits = []
        list_fits += str(fits)
        # convert str back to int
        for n1 in range(0, len(list_fits)):
            list_fits[n1] = int(list_fits[n1])

        # create key but FASTER
        multiplier = 1
        key_adapted = ''
        for n1 in list_fits[::-1]:

            while n1 > 0:
                n1 -= 1
                key_adapted += (key * multiplier)
            multiplier *= 10

    # conbine key and file
    encrypted = bytes(a ^ b for (a, b) in zip(data.encode(), key_adapted.encode()))

    # wite to disk
    #open(export_file, "wb").write(encrypted)
    return encrypted

    if motd:
        print(f'Process took: {process_time() - timer}')
