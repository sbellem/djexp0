from django.contrib import admin
from grafik.models import Graph, Point


class PointInline(admin.TabularInline):
    model = Point
    extra = 1


class GraphAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Publication date', {'fields': ['time'], 'classes': ['collapse']}),
    ]
    inlines = [PointInline]


admin.site.register(Graph, GraphAdmin)
