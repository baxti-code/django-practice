from django.shortcuts import render

def home(request):
    context = {
        'username': 'Baxtiyor',
        'role': 'Backend Developer'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'skills' : ['Django', 'Python', "HTML"],
        'is_developer' : True
              }
    return render(request, 'about.html', context)