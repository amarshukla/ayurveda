from django.db import models


class Inventory(models.Model):
    med_name = models.CharField(max_length=200)
    qty = models.IntegerField(default=1)
    expiry = models.DateField()
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.med_name
