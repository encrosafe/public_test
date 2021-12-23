from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def start_view(request):
	context['user'] = request.user
	template = loader.get_template('start_view.html')

	return HttpResponse(template.render(context, request))
