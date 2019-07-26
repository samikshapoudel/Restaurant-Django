from django.shortcuts import render, HttpResponse
from .forms import ContactUs
from django.core.mail import send_mail, BadHeaderError


# Create your views here.


def contactus(request):
    if request.method == 'GET':
        contact = ContactUs()
        return render(request, 'contactus/contactus.html', context={'contact': contact})

    else:
        contact_us_form = ContactUs(request.POST)
        if contact_us_form.is_valid():
            # print('Email: ', contact_us_form.cleaned_data['email'])
            # print('Phone:no:' , contact_us_form.cleaned_data['phone_no'])
            # print('query: ', contact_us_form.cleaned_data['query'])

            email =contact_us_form.cleaned_data['email']
            phone = contact_us_form.cleaned_data['phone_no']
            query = contact_us_form.cleaned_data['query']

            return HttpResponse('Submitted')
        else:
            return HttpResponse('Not Submitted')

