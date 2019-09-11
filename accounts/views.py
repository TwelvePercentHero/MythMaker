from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MythMakerForm

def register(request):
    return render(request, 'registration/register.html')

@login_required
def profile(request):
    username = request.user.username
    context = {'username' : username}
    return render(request, 'registration/profile.html', context)

def new_user(request):
    if request.method == 'POST':
        form = MythMakerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_date['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return render(request, 'registration/profile.html')
    else:
        form = MythMakerForm()
    return render(request, 'registration/register.html')


