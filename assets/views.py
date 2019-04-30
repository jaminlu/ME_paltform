from django.shortcuts import render
from assets import models

# Create your views here.

def assetlist(request):
    print("assetlist")
    return None


#@login_required
def assetinfo(request):
    print("assetsinfo")
    the_assets = models.Assets.objects.all()
    return render(request, 'assets/asset_info.html', locals())
    print(the_assets)
