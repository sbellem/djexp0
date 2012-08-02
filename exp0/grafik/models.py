import datetime

from django.db import models
from django.utils import timezone


class Graph(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField('publication date')

    def __unicode__(self):
        return self.name

    def recent(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

    recent.admin_order_field = 'time'
    recent.boolean = True
    recent.short_description = 'New?'


class Point(models.Model):
    graph = models.ForeignKey(Graph)
    x = models.DecimalField(max_digits=9, decimal_places=4)
    y = models.DecimalField(max_digits=9, decimal_places=4)

    def __unicode__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
