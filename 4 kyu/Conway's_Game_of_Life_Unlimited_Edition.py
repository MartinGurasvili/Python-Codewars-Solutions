def get_neighbours(x, y):
    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}

def get_generation(cells, generations):
    if not cells: return cells
    xm, ym, xM, yM = 0, 0, len(cells[0]) - 1, len(cells) - 1
    cells = {(x, y) for y, l in enumerate(cells) for x, c in enumerate(l) if c}
    for _ in range(generations):
        cells = {(x, y) for x in range(xm - 1, xM + 2) for y in range(ym - 1, yM + 2)
                    if 2 < len(cells & get_neighbours(x, y)) < 4 + ((x, y) in cells)}
        xm, ym = min(x for x, y in cells), min(y for x, y in cells)
        xM, yM = max(x for x, y in cells), max(y for x, y in cells)
    return [[int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)]
