from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sorted = request.GET.get('sort', 'name')
    context = {
        'phones': Phone.objects.order_by(sorted)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug__iexact=slug)
    }
    return render(request, template, context)
