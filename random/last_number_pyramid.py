from decode_message import create_pyramid


def get_last_numbers(pyramid):
    return [row[-1] for row in pyramid]


# Example usage:
rows = 4
pyramid = create_pyramid(rows)
last_numbers = get_last_numbers(pyramid)

print("Last numbers at the back of the pyramid:", last_numbers)
