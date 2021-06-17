from django.contrib import admin
from .models import Func
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
import re


class FuncAdmin(admin.ModelAdmin):
    @admin.display(description=_('Chart Image'))
    def image_tag(self, obj):
        """Showing chart image or error

        Args:
            obj ([object]): Function object

        Returns:
            HTML markup for image or error
        """
        pattern = '\/[\w]+\/[\w]+\.png'
        is_image = re.match(pattern, str(obj.chart_image))
        if is_image:
            return format_html('<img src="{}" style="width: 300px; height:200px; background-size:contain" />'.format(obj.chart_image.url))
        else:
            return format_html('<p>{}</p>'.format(obj.chart_image))

    list_display = ('func', 'image_tag', 'interval', 'dt', 'date')


admin.site.register(Func, FuncAdmin)
