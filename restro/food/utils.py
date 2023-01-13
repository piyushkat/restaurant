from django.core.mail import EmailMessage
import os


# sending email code configurations usng core email in python via smpt server
# importing other email details in dotenv file
class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=os.environ.get('EMAIL_FROM'),
      to=[data['to_email']]
    )
    email.send()