from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from forms import Authform, Regform


def login (request):
    args={}
    args.update(csrf(request))
    args['form'] = Authform()
    if request.POST:
        name = request.POST['username']
        pas = request.POST['password']
        user = auth.authenticate(username=name, password=pas)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['form'] = Authform(request.POST)
            args['error'] = 'We have no user with this attributes'
    return render_to_response('for_forms.html', args)


def logout (request):
    auth.logout(request)
    return redirect('/')


def register (request):
    args = {}
    args.update(csrf(request))
    args['form'] = Regform()
    if request.POST:
        frm = Regform(request.POST)
        if frm.is_valid():
            frm.save()
            newuser = auth.authenticate(username=frm.cleaned_data['username'],password=frm.cleaned_data['password1'])
            auth.login(request,newuser)
            return redirect('/')
        else:
            args['form'] = frm
    return render_to_response('for_forms.html', args)
