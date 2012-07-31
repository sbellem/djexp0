from django.db import models

class Graph(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField('time')

class Point(models.Model):
    graph = models.ForeignKey(Graph)
    x = models.DecimalField(max_digits=9, decimal_places=4)
    y = models.DecimalField(max_digits=9, decimal_places=4)
