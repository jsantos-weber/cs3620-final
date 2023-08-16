from django.shortcuts import render
from django.http import HttpResponse
from .models import NailData
from django.template import loader
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    template = loader.get_template('nailapp/home.html')
    return render(request, 'nailapp/home.html')


def nail_list(request):
    nail_object = NailData.objects.all()
    nail_name = request.GET.get('nail_name')
    if nail_name != '' and nail_name is not None:
        nail_object = nail_object.filter(name__icontains=nail_name)
    paginator = Paginator(nail_object, 4)
    page = request.GET.get('page')
    nail_object = paginator.get_page(page)
    return render(request, 'nailapp/nails.html', {'nail_object': nail_object})


def contact(request):
    template = loader.get_template('nailapp/contact.html')
    return render(request, 'nailapp/contact.html')


def detail(request, nail_id):
    nail_item = NailData.objects.get(pk=nail_id)
    context = {
        'nail_item': nail_item
    }
    return render(request, 'nailapp/detail.html', context)


def order(request):
    template = loader.get_template('nailapp/order.html')
    return render(request, 'nailapp/order.html')
