from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from message.models import Alter
from ManageEngine.api.req import request_user_id

# Create your views here.

@login_required()
def alert(request):
    alerts = Alter.objects.filter(to_user_id=request_user_id(request).order_by("gen_time"))
    num = alerts.count()
    return render(request, 'message/alter.html', locals())
