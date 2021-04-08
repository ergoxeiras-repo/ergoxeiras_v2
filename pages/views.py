from django.shortcuts import render
from django.core.mail import send_mail
from django.core.paginator import Paginator

from .forms import ContactForm
from .models import Image, Status

def indexView(request):
    images = Image.objects.order_by('-id')[:4]
    
    if request.method == 'POST':
        form = boundForm(request)
    else:
        form = unboundForm()

    return render(request, 'index.html', {'form': form, 'images': images})


def categoriesView(request):
    category = request.path[12:len(request.path)-1]
    
    greek_category = categoryInGreek(category)
    
    images = Image.objects.filter(category=category)

    paginator = Paginator(images, 2)
    
    page_number = request.GET.get('page')
    page_images = paginator.get_page(page_number)
    
    return render(request, 'categories.html', {
        'category': greek_category,
        'page_images': page_images
        })


def categoryInGreek(category):
    for categories in Status.choices:
        english_category, greek_category = categories
        if category == english_category:
            print('greek_category inside function is')
            print(greek_category)
            return greek_category


def boundForm(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        email_from = form.cleaned_data['email']
        
        send_mail(subject, body, email_from, ['christosglx@hotmail.com'],fail_silently=False,)
        
    return form


def unboundForm():
    form = ContactForm()
    return form
