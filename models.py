from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin


@python_2_unicode_compatible
class Slider(CMSPlugin):

    name = models.CharField(max_length=50)

    dots = models.BooleanField(default=False)

    fade = models.BooleanField(default=False)

    autoplay = models.BooleanField(default=True)

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Image(models.Model):

    slider = models.ForeignKey(
        Slider,
        related_name="images"
    )

    image = FilerImageField(
        null=True,
        blank=False
    )

    caption_text = models.CharField(
        null=True,
        blank=True,
        max_length=255
    )

    def __str__(self):
        if self.caption_text:
            return self.caption_text
        else:
            return self.image.label
