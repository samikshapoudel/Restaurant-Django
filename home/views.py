from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import WhyUs
# Create your views here.

def home(request):

    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    whyus = WhyUs.objects.all()


    context = {
        'meals':meals,
        'meal_list' :meal_list,
        'categories':categories,
        'posts':posts,
        'latest_post':latest_post,
        'whyus':whyus
    }

    return render(request, 'home/index.html', context)


