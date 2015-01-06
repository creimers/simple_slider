# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext as _

from .models import SliderPluginModel


class Slider(CMSPluginBase):

    model = SliderPluginModel
    name = _("Gallerie")
    render_template = "djangocms_gallerij/_gallery.html"

    def render(self, context, instance, placeholder):
        images = instance.slider.images.all()
        context.update({
            'images': images
        })

        return context

plugin_pool.register_plugin(Slider)
