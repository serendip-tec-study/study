from django.shortcuts import render
import json
import os

def createfunc(request):
    if request.method == 'POST':
        json_file = {
            'name': request.POST['name'],
            'department': request.POST['department'],
            'address': request.POST['address'],
            'phone': request.POST['phone'],
            'supplement': request.POST['supplement'],
        }
        path = os.getcwd() + '/templates/'
        
        with open(path + 'test.json', 'w') as f:
            json.dump(json_file, f, ensure_ascii=False)

    return render(request, 'create.html')

def viewfunc(request):
    return render(request, 'view.html')

def jsonfunc(request):
    return render(request, 'test.json')