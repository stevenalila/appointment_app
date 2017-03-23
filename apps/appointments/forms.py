from django import forms
from .models import Appointment
from django.utils.timezone import now

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['name', 'task', 'datetime', 'status']

	def clean_datetime(self):
		datetime = self.cleaned_data['datetime']
		if now() > datetime:
			raise forms.ValidationError("Kindly update time to future tense")
		return datetime