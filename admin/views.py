from django.shortcuts import render, HttpResponse

def painel_admin(request):
    return render(request, 'painel_admin.html')