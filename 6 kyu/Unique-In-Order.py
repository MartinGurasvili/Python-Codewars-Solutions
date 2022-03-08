def unique_in_order(iterable):
    array = []
    last_val = str()
    for x in range (0, len(iterable)):
        if iterable[x] != last_val:
            last_val = iterable[x]
            array.append(iterable[x])
    return array
