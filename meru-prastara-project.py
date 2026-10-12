def generate_meru_prastara(n):
    """Generate n rows of Meru-Prastara (Pascal Triangle)."""

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def print_meru_prastara(n):
    triangle = generate_meru_prastara(n)

    if n == 0:
        print("(empty triangle)")
        return

    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        text = " ".join(map(str, row))
        print(text.center(width))


n = 6
print_meru_prastara(n)
