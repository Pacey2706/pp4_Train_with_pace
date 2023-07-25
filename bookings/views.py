from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


# views go here
@login_required
def dashboard(request, id):
    context = {'id': id}
    return render(request, 'bookings/dashboard.html/', context)


@login_required
def update_client(request, id):
    client = Client.objects.get(id=id)
    if request.user == client.user:
        # If requested user is client user return/process form
        if request.method == "post":
            form = ClientForm(request.post, instance=client)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("dashboard", id)
                except Exception:
                    context = {"form": form}
                    return render(request,
                                  "bookings/client_form.html",
                                  context)

        else:
            form = ClientForm(instance=client)

    else:
        # if the requested user is not client user,
        # redirect user to the correct profile
        id = request.user.id
        return redirect("update-client", id)
    
    context = {"form": form}
    return render(request, "bookings/client_form.html", context)


