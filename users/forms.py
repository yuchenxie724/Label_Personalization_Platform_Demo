from django import forms

from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'labels'
		]


class RawUserForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs = {"placeholder": "Your username"}))
	labels = forms.CharField(required = False)
