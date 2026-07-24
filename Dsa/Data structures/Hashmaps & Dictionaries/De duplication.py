emails_acc = [
    'hayyanwebdev@gmail.com',
    'bleh@gmail.com',
    'farhan@gnail.com'
    'bleh@gmail.com',
    'huzaifa@gmail.com',
    'imrhamza17@gmail.com',
    'bleh@gmail.com'
]

def remove_duplictes(emails):
    seen_emails = set()
    unique_emails = []

    for email in emails:
        if email not in seen_emails:
            unique_emails.append(email)
            seen_emails.add(email)

    return unique_emails

mails = remove_duplictes(emails_acc)
print(mails)