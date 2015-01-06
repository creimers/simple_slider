from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey


class Slider(CMSPlugin):

    name = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __unicode__(self):
        return u'%s' % self.name


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

    def __unicode__(self):
        if self.caption_text:
            return u'%s' % self.caption_text
        else:
            return u'%s' % self.image.label
