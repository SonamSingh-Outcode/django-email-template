from threading import Thread

from django.core.mail import send_mail
from django.template.loader import render_to_string

from config.settings import FROM_EMAIL


def email_sender(template, context, subject, recipient_list):
    message = render_to_string(template, context)
    EmailThread(subject=subject, html_content=message, recipient_list=recipient_list).start()


class EmailThread(Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        Thread.__init__(self)

    def run(self):
        send_mail(subject=self.subject, message='',
                  from_email=FROM_EMAIL,
                  recipient_list=self.recipient_list,
                  html_message=self.html_content)
