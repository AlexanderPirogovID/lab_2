import re

def info(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
    capital_word_pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]*\b'
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    capital_words = re.findall(capital_word_pattern, text)

    with open('emails.txt', 'w', encoding='utf-8') as email_file:
        for email in emails:
            email_file.write(email + '\n')
    with open('phones.txt', 'w', encoding='utf-8') as phone_file:
        for phone in phones:
            phone_file.write(phone + '\n')
    with open('capital_words.txt', 'w', encoding='utf-8') as capital_file:
        for word in capital_words:
            capital_file.write(word + '\n')
    print("done")

info('text.txt')