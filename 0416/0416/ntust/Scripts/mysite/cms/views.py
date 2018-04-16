from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

from .models import Profile, ProfileIntro

def index(request):
	profiles = Profile.objects.all()
	return render_to_response('cms/menu.html',locals())