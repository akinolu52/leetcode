import re


def is_valid_email(word):
    pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)"
    return re.findall(pattern, word)


def write_emails_to_text(content):
    try:
        # open file it exist or create the file if it doesn't exist
        # and write to the file
        with open('extracted_email.txt', 'w') as file:
            for email in content:
                file.write(f"{email}\n")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
   
    print("Content successfully written to the file.")


def extract_email(text_file):
    try:
        # open the file
        with open(text_file, 'r') as file:
            lines = file.readlines()
            emails = []

            # loop through each lines
            for line in lines:
                if valid_emails := is_valid_email(line):
                    emails.extend(valid_emails)

            # write the emails to a txt file
            write_emails_to_text(emails)

            return f"{len(emails)} Emails found: {', '.join(emails)}"
        
    except FileNotFoundError:
        print(f"Error: File '{text_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


txt_file = '/Users/mac/Desktop/web/frontend/leetcode/random/Q1_Extract_emails.txt'
print(extract_email(txt_file))
