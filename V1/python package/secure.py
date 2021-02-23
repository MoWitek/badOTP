def secure(data="Lorem Ipsum", buffer=512, custom_buffer=None):
    from random import choice

    buffer_data = ["+", "-", "*", "/", "q", "w", "e", "r", "t", "z"]
    if custom_buffer is not None:
        buffer_data = custom_buffer

    # make long enough key
    data_secured = data
    for n in range(0, buffer):
        data_secured += choice(buffer_data)
    data_secured += choice(buffer_data)[0:buffer]

    return data_secured

