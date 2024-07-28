import yagmail
import os

username = os.getenv('EMAIL_USERNAME')
password = os.getenv('EMAIL_PASSWORD')
pr_author = os.getenv('PR_AUTHOR')

# Email content
subject = 'Thank you for your contribution!'
contents = f'Thank you, {pr_author}, for your contribution to our repository. Your PR has been successfully merged!'

# Sending the email
yag = yagmail.SMTP(user=username, password=password)
yag.send(to=username, subject=subject, contents=contents)
