from django.shortcuts import render

def hello_world(request):
    return render(request, '../templates/hello_world.html', {})