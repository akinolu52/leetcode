
def open_and_read(file_name):
    try:
        # open the file and return the lines in the file
        with open(file_name, 'r') as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_content(index, content1, content2):
    """
    Check the content of two inputs and print the different words.

    Args:
        index (int): The index of the content.
        content1 (str): The first content to compare.
        content2 (str): The second content to compare.

    Returns:
        None

    Examples:
        >>> check_content(0, "Hello world", "Hello everyone")
        line number: 1
        1 words matched
        1 words do not match
        words that do not match includes: everyone
    """
    line1 = set(content1.lower().split())
    line2 = set(content2.lower().split())

    same_words = line1.intersection(line2)
    if different_words := line1.symmetric_difference(line2):
        print_different_words(
            index, same_words, len(different_words), different_words)


def print_different_words(index, same_words, count_different_words, different_words):
    """
    Print the line number, count of matched words, count of different words, and the different words.

    Args:
        index (int): The index of the line.
        same_words (set): The set of words that are present in both lines.
        count_different_words (int): The count of words that are different between the lines.
        different_words (iterable): The iterable containing the different words.

    Returns:
        None
    """
    print(f"line number: {index + 1}")
    count_same_words = len(same_words)
    print(f"{count_same_words} words matched")
    print(f"{count_different_words} words do not match")
    different_words_str = ', '.join(different_words)

    print(
        f"words that do not match includes: {different_words_str}\n\r")


def compare_word_in_line(file_1, file_2):
    """
    Compare the content of two files and check for word matches and differences.

    Args:
        file_1 (str): The path to the first file.
        file_2 (str): The path to the second file.

    Returns:
        None
    """
    content1 = open_and_read(file_1)
    content2 = open_and_read(file_2)

    content1_len = len(content1)
    content2_len = len(content2)
    count = max(content1_len, content2_len)

    index = 0

    while index < count:
        if index < content1_len and index < content2_len:
            check_content(index, content1[index], content2[index])

        elif index > content1_len:
            check_content(index, set(), content2[index])

        elif index > content2_len:
            check_content(index, set(), content1[index])

        index += 1
    return


file_1 = '/Users/mac/Desktop/web/frontend/leetcode/random/Q2_text_file_1.txt'
file_2 = '/Users/mac/Desktop/web/frontend/leetcode/random/Q2_text_file_2.txt'
print(word_in_line_compare(file_1, file_2))
