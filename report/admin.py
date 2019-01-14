from django.contrib import admin

# Register your models here.

from .models import Quarter
from .models import QuarterReport
from .models import SectorPerformance

admin.site.register(Quarter)
admin.site.register(QuarterReport)
admin.site.register(SectorPerformance)
