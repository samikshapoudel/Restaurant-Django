from django.shortcuts import render
from .models import AboutUs, WhyUs, Chef
# Create your views here.

def aboutus_list(request):
    about = AboutUs.objects.last()
    whyus = WhyUs.objects.all()
    chef = Chef.objects.all()


    context = {

        'about':about,
        'whyus': whyus,
        'chef': chef
    }

    return render(request, 'aboutus/about.html', context)