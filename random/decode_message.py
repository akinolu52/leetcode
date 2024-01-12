
def sequence_term(n):
    if n == 1:
        return [1]

    current_sum = 1
    result = [1]

    for current_addend, _ in enumerate(range(1, n), start=2):
        if current_sum > n:
            break
        current_sum += current_addend
        result.append(current_sum)

    return result


def sorted_decoded_words(decoded_words):
    return dict(sorted(decoded_words.items()))


def decode(message_file):
    try:
        with open(message_file, 'r') as file:
            lines = file.readlines()
            needed_lines = sequence_term(len(lines))

            decoded_words = {}

            for line in lines:
                words = line.split()
                selected_word_index = int(words[0])

                if selected_word_index in needed_lines:
                    selected_word = words[-1].strip().lower()
                    decoded_words[selected_word_index] = selected_word

            return ' '.join(sorted_decoded_words(decoded_words).values())
    except FileNotFoundError:
        print(f"Error: File '{message_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


print(decode("/Users/mac/Desktop/web/frontend/leetcode/random/coding_message_text.txt"))
print()
print(decode("/Users/mac/Desktop/web/frontend/leetcode/random/coding_qual_input.txt"))
