from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Asset(models.Model):
    status_choices = [
        ('assigned', 'Assigned'),
        ('unassigned', 'Unassigned'),
        ('maintenance', 'Under Maintenance'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
    ]
    tag = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default='unassigned')
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.tag

class AssetAssignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.asset
