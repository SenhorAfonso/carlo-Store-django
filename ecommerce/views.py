from django.shortcuts import render, HttpResponse

def ecommerce(request):
    return render(request, 'ecommerce.html')
