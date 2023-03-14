from django.db import models

class linkdetailM(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=250)
    date = models.TextField(max_length=50)
    risk = models.TextField(max_length=50)
    cve = models.TextField(max_length=50)
    cwe = models.TextField(max_length=50)