from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


class Email(object):

    def send(self):
        name = self['name']
        email = self['email']
        phone = self['phone']
        city = self['city']
        solution = self['solution']
        message = self['message']

        body = render_to_string(
            'email.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'city': city,
                'message': message
            }
        )
        subject = name + '-' + solution

        from_mail = settings.EMAIL_HOST_USER

        email_message = EmailMessage(
            subject,
            body,
            from_mail,
            ['info@messiersolutions.com'],
        )

        email_message.content_subtype = 'html'
        email_message.send(fail_silently=False)

        return 'Se envió exitosamente'
