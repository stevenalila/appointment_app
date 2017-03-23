from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment  # Added this line
from django.forms import ModelForm
from .forms import AppointmentForm
from django.utils.timezone import now


# Create your views here.
@login_required
def create(request):
	form = AppointmentForm(request.POST or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('index')
	return render(request, "appointments/create.html", {'form': form})


@login_required
def edit(request, id):
	appointment = get_object_or_404(Appointment, id=id)
	form = AppointmentForm(request.POST or None, instance=appointment)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, "appointments/edit.html", {'form':form})


@login_required
def index(request):
	today = now().today()
	today_appointments = Appointment.objects.filter(user=request.user, datetime__year=today.year, datetime__month=today.month, datetime__day=today.day)
	tomorrow_appointments = Appointment.objects.filter(user=request.user).exclude(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day)
	return render(request, "appointments/index.html", { 
		'today_appointments':today_appointments, 
		'tomorrow_appointments':tomorrow_appointments,
		'current_date':now()})


@login_required
def delete(request, id):
	appointment = get_object_or_404(Appointment, id=id)
	if request.method=='POST':
		appointment.delete()
		return redirect('index')
	return render(request, "appointments/delete.html", {'object':appointment})

