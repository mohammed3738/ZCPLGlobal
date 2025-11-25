from django.db import models

# Create your models here.




class CaseStudyCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Case Study Category"
        verbose_name_plural = "Case Study Categories"

    def __str__(self):
        return self.name


from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class CaseStudy(models.Model):
    category = models.ForeignKey(
        CaseStudyCategory, on_delete=models.SET_NULL, null=True, related_name="projects"
    )

    title = models.CharField(max_length=255)
    short_description = models.TextField()
    detailed_description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='casestudies/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Ensure slug uniqueness
            while CaseStudy.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
