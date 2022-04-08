from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from builtins import object

class UserForm(forms.ModelForm):
	password2 = forms.CharField(widget=forms.PasswordInput())

	class Meta(object):
		model = User
		fields = [
			'username',
			'email',
			'password',
		]

	def clean():
		cleaned_data = super().clean()

		username = cleaned_data.get('username')

		for user in User.objects.all():
			if user.username == username:
				raise ValidationError(
					'Der Nutzername ist bereits vergeben'
				)

		p1 = cleaned_data.get('password')
		p2 = cleaned_data.get('password2')

		if p1 != p2:
			raise ValidationError(
				'Die Passwörter sind nicht identisch'
			)