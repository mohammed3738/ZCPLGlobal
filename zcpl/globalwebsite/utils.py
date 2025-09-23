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
