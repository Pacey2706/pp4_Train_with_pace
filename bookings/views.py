from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Client, Booking, Session
from .forms import ClientForm, BookingForm, SessionForm


# views go here
@login_required
def dashboard(request, id):
    # get user object for that id
    user = User.objects.get(id=id)
    # get the client object for that user
    try:
        client = Client.objects.get(user=user)
        bookings = Booking.objects.filter(client=client.id)
    except Exception:
        client = None
    # then add clinet id to context
    context = {'id': id, "client": client.id, "bookings": bookings}
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


@login_required
def book_session(request, session):
    if session == "1":
        session_obj = get_object_or_404(Session, duration=30)
    elif session == "2":
        session_obj = get_object_or_404(Session, duration=60)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            client = get_object_or_404(Client, user=request.user)
            booking = form.save(commit=False)
            booking.session = session_obj

            booking.client = client
            booking.save()
            return redirect("dashboard", request.user.id)

    else:
        form = BookingForm()

    context = {"form": form, "session": session, "session_obj": session_obj}
    return render(request, "bookings/booking_form.html", context)


@login_required
def select_session(request, id):
    # get form
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            selected_session = form.cleaned_data["option"]
            return redirect("booking-form", selected_session)
    else:
        form = SessionForm()

    context = {
        "form": form,
        "client_id": id,
    }
    return render(request, "bookings/session_form.html", context)
    # if form is valid

    # redirect passing through session value
    # otherwise put form in context and clinet_id
    # render form
