from django.db import models

# Create your models here.


from django.utils import timezone

class APeriod(models.Model):
    name = models.CharField(max_length = 200)
    start = models.DateTimeField()
    end = models.DateTimeField
    
    def __str__(self):
        return self.name
        
    class Meta:
        abstract = True
        
class Quarter(APeriod):
    code =models.CharField(max_length = 12)

class AReport(models.Model):
    name = models.CharField(max_length=200,default = 'Report')
    
    def __str__(self):
        return self.name
        
    class Meta:
        abstract = True

class QuarterReport(AReport):
    period = models.ForeignKey('Quarter', on_delete=models.CASCADE)
    code = models.CharField(max_length = 12)
    
class AssetPerformance(models.Model):
    name = models.CharField(max_length=200)
    rtn = models.DecimalField(max_digits=8,decimal_places=4) # the return on the asset
    mv = models.DecimalField(max_digits=12,decimal_places=4) # the market value of the asset
    
    def __str__(self):
        return self.name
        
    class Meta:
        abstract=True
        
class SectorPerformance(AssetPerformance):
    code = models.CharField(max_length = 12)
