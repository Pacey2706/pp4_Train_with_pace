from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Client
from .forms import ClientForm


# views go here
@login_required
def dashboard(request, id):
    # get user object for that id
    user = User.objects.get(id=id)
    # get the client object for that user
    try:
        client = Client.objects.get(user=user)
    except Exception:
        client = None
    # then add clinet id to context
    context = {'id': id, "client": client.id}
    return render(request, 'bookings/dashboard.html/', context)


@login_required
def update_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.user == client.user:
        # If requested user is client user return/process form
        if request.method == "POST":
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                try:
                    print('trying to save')
                    form.save()
                    return redirect("dashboard", request.user.id)
                except Exception:
                    context = {"form": form, "client": client}
                    return render(request,
                                  "bookings/client_form.html",
                                  context)
            else:
                print('form not valid')

        else:
            form = ClientForm(instance=client)

    else:
        # if the requested user is not client user,
        # redirect user to the correct profile
        return redirect("update-client", client.user.id)
    
    context = {"form": form, "client": client}
    return render(request, "bookings/client_form.html", context)


