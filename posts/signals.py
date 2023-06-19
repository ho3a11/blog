from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)