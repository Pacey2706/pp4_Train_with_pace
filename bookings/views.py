from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


# views go here
@login_required
def dashboard(request, id):
    context = {'id': id}
    return render(request, 'bookings/dashboard.html/', context)
