from django.shortcuts import render

def register(request):
    return render(request, 'registration/register.html')

def profile(request):
    username = request.user.username
    context = {'username' : username}
    return render(request, 'registration/profile.html', context)


