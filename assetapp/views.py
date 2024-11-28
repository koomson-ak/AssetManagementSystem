from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssetForm, UserForm
from .models import Asset, User, AssetAssignment

# Create your views here.

def asset_view_detailed(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    asset_assignment = get_object_or_404(AssetAssignment, asset=asset)
    user = asset_assignment.user
    context = {
        'tag': asset.tag,
        'category': asset.category,
        'type': asset.type,
        'owner': user.name,
        'departmenet': user.department,
        'status': asset.status,
        'note': asset.notes,
        'date_added': asset.date_added,
        'date_updated': asset.date_updated,
    }
    return render(request, 'detailed_view.html', context)

def assets(request):
    queryset = Asset.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'assetapp/templates/assets.html', context)