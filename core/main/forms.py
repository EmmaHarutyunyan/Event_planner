
from django import forms
from django import forms
from django.contrib.auth.models import User
from .models import Booking, Event
from .models import Contact

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event', 'date', 'time']

    event = forms.ModelChoiceField(queryset=Event.objects.all(), widget=forms.Select(attrs={'class': 'event-select'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
