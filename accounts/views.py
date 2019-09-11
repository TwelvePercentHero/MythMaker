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

def register(request):
    if request.method == 'POST':
        form = MythMakerForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = MythMakerForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


