from django.shortcuts import render
def forloop(request):
    d={'name':'pavi'}
    return render(request,'forloop.html',d)
