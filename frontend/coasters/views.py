from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    order_status = request.GET.get('order_status', '')
    return render(request, "coasters/index.html", {'order_status': order_status})

def engrave(request):
    if request.method == "GET":
        name = request.GET.get('name')
        design = request.GET.get('design')
        response_text = f"Name: {name}, Design: {design}"
        return redirect(f'/?order_status={response_text}')
    return HttpResponse("Invalid request method", status=405)
