from django.db import models

# Create your models here.


from django.utils import timezone

class Quarter(models.Model):
    name = models.CharField(max_length = 200)

class Report(models.Model):
    quarter = models.ForeignKey('Quarter', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class AssetPerformance(models.Model):
    report = models.ForeignKey('Report', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rtn = models.DecimalField(max_digits=8,decimal_places=4) # the return on the asset
    mv = models.DecimalField(max_digits=12,decimal_places=4) # the market value of the asset
    comment = models.TextField(default = "No comments.")
    graph = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
