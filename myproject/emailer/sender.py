from emailer.utils import prepare_and_send_email


def send_signup_success_email(user):
    """
    Notify user about successful signup.
    """
    prepare_and_send_email(
        user=user,
        template_name='signup_success',
    )
