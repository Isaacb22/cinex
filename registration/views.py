from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.

class SignUpView(CreateView):
	form_class = UserCreationFormWithEmail
	template_name = 'registration/signup.html'

	def get_success_url(self):
		return reverse_lazy('login') + '?register'

	def get_form(self, form_class=None):
		form = super(SignUpView, self).get_form()
		# Modificar en tiempo real
		form.fields['username'].widget = forms.TextInput(
			attrs={'class':'input100', 'placeholder':'Nombre de usuario'})
		form.fields['email'].widget = forms.EmailInput(
			attrs={'class':'input100', 'placeholder':'Direccion email'})
		form.fields['password1'].widget = forms.PasswordInput(
			attrs={'class':'input100', 'placeholder':'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(
			attrs={'class':'input100', 'placeholder':'Repita la contraseña'})
		return form