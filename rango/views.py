from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Hello!"}
    return render(request, 'rango/about.html', context = context_dict)
    return HttpResponse("Rango says here is the about page")

def show_category(request, category_name_slug):
    # Create a context dictionary, which we can pass to the template rendering engine
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        # retrueve all of the associated pages, filter will return a list of objects
        pages = Page.objects.filter(category=category)
        # adds our results list to the template under name pages
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        #we get here if we didn't fine the specified category
        #the template will display the "no category" message for us
        context_dict['category'] = None
        context_dict['pages'] = None
    #go render the response and return it to the client
    return render(request, 'rango/category.html', context_dict)


