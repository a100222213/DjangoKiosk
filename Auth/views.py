from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Menu.models import M_Menu
from django.core import serializers

# Create your views here.
def V_Login(request):
	auth.logout(request)
	return  render(request, 'login.html')


def V_CheckAuth(request):
	username = request.POST.get('inputEmail', '')
	password = request.POST.get('inputPassword', '')
	user = auth.authenticate(username=username, password=password)


	if user is not None and user.is_active:
		auth.login(request, user)

		try:
			MenuData=M_Menu.objects.filter(IsActive=True)
			#request.session['Menu']=MenuData.values_list()
			request.session['Menu']=serializers.serialize('json', MenuData, fields=('id','MenuName','MenuLink','MenuType','MenuParent','MenuIcon'))
		except:
			request.session['Menu']=null

		if user.is_superuser:
			return HttpResponseRedirect('/admin/')
		else:
			return render(request, 'index.html')

	else:
		return render(request, 'index.html')


def V_ClearSession(request):
	del request.session['Menu']
	try:
		MenuData=M_Menu.objects.filter(IsActive=True)
		#request.session['Menu']=MenuData.values_list()
		request.session['Menu']=serializers.serialize('json', MenuData, fields=('id','MenuName','MenuLink','MenuType','MenuParent','MenuIcon'))
	except:
		request.session['Menu']=null
	return redirect('/home/')
