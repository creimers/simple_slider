# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from adminsortable.admin import SortableStackedInline

from django.utils.translation import ugettext as _

from .models import (
    SliderPluginModel,
    Image
)


class ImageInline(SortableStackedInline):
    model = Image
    extra = 1


class Slider(CMSPluginBase):

    model = SliderPluginModel
    name = _("Gallerie")
    render_template = "djangocms_simple_slider/_slider.html"
    inlines = [ImageInline, ]

    def render(self, context, instance, placeholder):
        images = instance.slider.images.all()
        context.update({
            'images': images
        })

        return context

plugin_pool.register_plugin(Slider)
