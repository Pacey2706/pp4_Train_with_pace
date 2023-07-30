from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Client, Booking, Session
from .forms import ClientForm, BookingForm, SessionForm, BookingDayForm, BookingTimeForm


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
    context = {'id': id, "client": client, "bookings": bookings}
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
    if request.method == "POST":
        day_form = BookingDayForm(request.POST)
        if day_form.is_valid():
            selected_day = day_form.cleaned_data["day"]
            request.session["selected_day"] = str(selected_day)
            return redirect("select-booking-time", session)

    else:
        day_form = BookingDayForm()
    context = {"day_form": day_form, "session": session}
    return render(request, "bookings/booking_form_day.html", context)


@login_required
def select_booking_time(request, session):
    selected_day = request.session.get("selected_day")
    print(selected_day)
    if not selected_day:
        return redirect("select-session", id=request.user.id)

    if request.method == "POST":
        time_form = BookingTimeForm(request.POST)
        if time_form.is_valid():
            selected_time = time_form.cleaned_data["time"]
            if session == "1":
                duration = 30
            elif session == "2":
                duration = 60
            session_obj = get_object_or_404(Session, duration=duration)
            client = get_object_or_404(Client, user=request.user)
            booking = Booking.objects.create(session=session_obj, client=client, date=selected_day, time=selected_time)
            return redirect("dashboard", request.user.id)

    else:
        time_form = BookingTimeForm()

    context = {"time_form": time_form, "session": session, "selected_day": selected_day}
    return render(request, "bookings/booking_form_time.html", context)


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


@login_required
def delete_session(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        return redirect("dashboard", request.user.id)
    else:
        context = {"booking": booking}
        return render(request, "bookings/delete_booking_form.html", context)

