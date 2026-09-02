from django.db import models

# Create your models here.


from django.urls import reverse



from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


#**************************Vaishnavi FAQ Model

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class FAQ(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="casestudy_faq_content_types"
    )
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    question = models.TextField()
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.question
    
#**************************Vaishnavi FAQ Model End


class CaseStudy(models.Model):
    faqs = GenericRelation(
        FAQ,
        related_query_name='casestudy'
    )
    title = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_desc = models.TextField(blank=True, null=True)

    short_description = models.TextField()
    detailed_description = RichTextUploadingField()

    thumbnail = models.ImageField(upload_to='casestudies/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto slug generation
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while CaseStudy.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Auto fill meta title if empty
        if not self.meta_title:
            self.meta_title = self.title

        # Auto fill meta description if empty
        if not self.meta_desc:
            self.meta_desc = self.short_description[:160]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("case_study_detail", args=[self.slug])
