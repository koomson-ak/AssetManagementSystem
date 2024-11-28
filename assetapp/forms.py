from django import forms
from .models import Asset, User, AssetAssignment
from django.contrib.contenttypes import fields

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['tag', 'category', 'type', 'owner', 'notes']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'department']

class AssetAssignmentForm(forms.ModelForm):
    class Meta:
        model = AssetAssignment
        fields = ['asset', 'user']
