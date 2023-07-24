from django.shortcuts import render

# Create your views here.


def home(request):
    # View to handle home page requests
    context = {}
    return render(request, "train_with_pace/index.html", context)


def services(request):
    # View to handle home page requests
    context = {}
    return render(request, "train_with_pace/services.html", context)


def contact(request):
    # View to handle home page requests
    context = {}
    return render(request, "train_with_pace/contact.html", context)
