from django.db import models
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from .tasks import get_chart
from django.utils.translation import gettext_lazy as _


class Func(models.Model):
    func = models.CharField(
        verbose_name=_('function'),
        max_length=120
    )
    chart_image = models.ImageField(
        verbose_name=_('chart_image'),
        upload_to='chart_pics',
        default='chart_pics/sample_image.png'
    )
    interval = models.IntegerField(
        verbose_name=_('interval'),
        default=1
    )
    dt = models.IntegerField(
        verbose_name=_('dt'),
        default=1
    )
    date = models.DateTimeField(
        verbose_name=_('date updated'),
        auto_now=True
    )

    def __str__(self):
        return self.func

    def save(self, *args, **kwargs):
        """Overrides save() method
        """
        super().save(*args, **kwargs)  # Call the "real" save() method.
        task_result = get_chart.apply_async(
            (self.func, self.interval, self.dt, self.id),
            countdown=5
        )
        task_value = task_result.get()
        Func.objects.filter(id=self.id).update(chart_image=task_value)
