from django.utils.text import slugify
from datetime import datetime

def custom_filename(filename):
    """
    Generate upload path for CKEditor images.
    """
    # Default slug if no blog yet
    slug = "general"

    # Try to infer from request (last saved blog)
    from globalwebsite.models import Blog
    last_blog = Blog.objects.last()
    if last_blog:
        slug = slugify(last_blog.title)

    today = datetime.now().strftime("%Y/%m/%d")
    return f"uploads/blogs/{slug}/{today}/{filename}"






import logging

from django.conf import settings
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)


def send_lead_email(subject, message, recipients=None, attachments=None):
    """
    Send a form-submission notification email.

    `attachments` is an optional list of uploaded files.
    Never raises: the lead is already saved in the DB, so an SMTP problem
    must not turn a successful submission into a 500 for the visitor.
    """
    recipients = recipients or settings.CONTACT_RECIPIENTS
    try:
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
        for f in attachments or []:
            email.attach(f.name, f.read(), getattr(f, "content_type", None))
        email.send(fail_silently=False)
        return True
    except Exception:
        logger.exception("Failed to send lead email %r to %s", subject, recipients)
        return False
