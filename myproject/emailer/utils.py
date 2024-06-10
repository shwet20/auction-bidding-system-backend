from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def prepare_and_send_email(user, template_name, data={}, **kwargs):
    """
    Prepare and send an email to the user.
    user: The user to whom the email is to be sent.
    template_name: The name of the folder that contains the email
    message.html & subject.txt inside 'emailer.templates'.
    data: A dictionary of data to be passed to the template.

    Optional kwargs -
    recipient_list: A list of recipients.
    from_email: The email address to be used as the sender.
    """

    context = {
        'user': user,
        'settings': settings,
        'data': data,
    }

    # Preparing sender & recipient
    if not kwargs.get('recipient_list'):
        kwargs['recipient_list'] = [user.email]

    if not kwargs.get('from_email'):
        kwargs['from_email'] = settings.DEFAULT_EMAIL_SENDER

    # Preparing message & subject
    html_message_template = '{}/message.html'.format(template_name)
    subject_template = '{}/subject.txt'.format(template_name)

    html_message = render_to_string(html_message_template, context=context)
    subject = render_to_string(subject_template, context=context)

    # Sending email
    send_mail(
        subject=subject,
        message="",
        fail_silently=False,
        html_message=html_message.strip(),
        **kwargs,
    )
