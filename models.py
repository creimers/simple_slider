from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey


@python_2_unicode_compatible
class Slider(CMSPlugin):

    name = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str_-(self):
        return self.name


@python_2_unicode_compatible
class Image(Sortable):
    class Meta(Sortable.Meta):
        pass

    slider = SortableForeignKey(
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

    def __str_-(self):
        if self.caption_text:
            return self.caption_text
        else:
            return self.image.label
