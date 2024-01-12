def create_pyramid(rows):
    pyramid = []

    current_number = 1

    for i in range(rows):
        row = []

        for _ in range(i + 1):
            row.append(current_number)
            current_number += 1

        pyramid.append(row)

    return pyramid


def print_pyramid(pyramid):
    for row in pyramid:
        print(" ".join(map(str, row)))


# Example usage:
rows = 4
pyramid = create_pyramid(rows)
print_pyramid(pyramid)
