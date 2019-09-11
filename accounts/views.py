from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, 'registration/register.html')

@login_required
def profile(request):
    username = request.user.username
    context = {'username' : username}
    return render(request, 'registration/profile.html', context)


