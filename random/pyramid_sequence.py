
# 1 3 5 10 15 21 28 36 45 55

def sequence_term(n):
    if n == 1:
        return [1]

    current_sum = 1  # Initialize with the first term
    result = [1]

    for current_addend, _ in enumerate(range(1, n), start=2):
        current_sum += current_addend
        result.append(current_sum)

    return result


for n in range(1, 11):
    result = sequence_term(n)
    print(f"The {n}th term in the sequence is: {result}")
