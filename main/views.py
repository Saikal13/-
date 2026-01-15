from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Service, Doctor, Review
from .forms import AppointmentForm

def home(request):
    services = Service.objects.all()
    doctors = Doctor.objects.all()
    reviews = Review.objects.all()
    return render(request, 'main/home.html', {
        'services': services,
        'doctors': doctors,
        'reviews': reviews
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/doctors.html', {'doctors': doctors})

def contacts(request):
    return render(request, 'main/contacts.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            send_mail(
                'Запись подтверждена',
                f'Спасибо, {appointment.name}! Ваша запись подтверждена на {appointment.date} {appointment.time}.',
                'clinic@example.com',
                [appointment.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'main/appointment.html', {'form': form})
