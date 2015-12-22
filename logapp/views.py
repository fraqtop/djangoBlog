from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from forms import Authform

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
    return render_to_response('mylogin.html',args)


def logout (request):
    auth.logout(request)
    return redirect('/')