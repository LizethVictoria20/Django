from django.conf import settings
from django.shortcuts import render
from django.core.mail   import send_mail
from django.http import HttpResponse

from uno.forms import ContactForm


def index(request):

	return render (request,  'index.html')


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email= form.cleaned_data.get('email')
		form_mensaje= form.cleaned_data.get('mensaje')
		form_nombre= form.cleaned_data.get('nombre')
		asunto= 'from de contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje= '%s: %s enviado por %s '%(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently = True
			)
	context = {
	'form':form
	}

	return  render (request, 'forms.html', context)


def about (request):
	return render(request, 'about.html')