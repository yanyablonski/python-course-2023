list_of_emails = []

email_str = None

emails = {
            'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
            'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
            'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
            'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
            'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
            'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
        }
for value in emails['mgu.edu']:
    email_str = value + '@' + 'mgu.edu'
    list_of_emails.append(email_str)

for value in emails['gmail.com']:
    email_str = value + '@' + 'gmail.com'
    list_of_emails.append(email_str)

for value in emails['msu.edu']:
    email_str = value + '@' + 'msu.edu'
    list_of_emails.append(email_str)

for value in emails['yandex.ru']:
    email_str = value + '@' + 'yandex.ru'
    list_of_emails.append(email_str)

for value in emails['harvard.edu']:
    email_str = value + '@' + 'harvard.edu'
    list_of_emails.append(email_str)

for value in emails['mail.ru']:
    email_str = value + '@' + 'mail.ru'
    list_of_emails.append(email_str)

list_of_emails.sort()
print(list_of_emails)