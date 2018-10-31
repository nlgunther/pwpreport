from django.contrib import admin

# Register your models here.

from .models import Quarter
from .models import Report
from .models import AssetPerformance

admin.site.register(Quarter)
admin.site.register(Report)
admin.site.register(AssetPerformance)
