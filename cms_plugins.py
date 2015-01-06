# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from adminsortable.admin import SortableStackedInline

from django.utils.translation import ugettext as _

from .models import (
    Slider,
    Image
)


class ImageInline(SortableStackedInline):
    model = Image
    extra = 1


class SliderPlugin(CMSPluginBase):

    model = Slider
    name = _("Simple Slider")
    render_template = "djangocms_simple_slider/_slider.html"
    inlines = [ImageInline, ]

    def render(self, context, instance, placeholder):
        images = instance.slider.images.all()
        context.update({
            'images': images
        })

        return context

plugin_pool.register_plugin(SliderPlugin)
