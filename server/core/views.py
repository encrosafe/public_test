from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def start_view(request):
	context = {
		'user': request.user
	}
	template = loader.get_template('start_view.html')

	return HttpResponse(template.render(context, request))


def check_login_and_redirect(request):
	try:
		if request.user:
			return redirect('start_view')
		else:
			return redirect('login')
	except:
		return redirect('login')