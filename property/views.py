from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render
from django.db.models import Q
from .models import *


def index(request):

    recommended = ObjectProperty.objects.filter(recommended=True)

    return render(
        request,
        'neruhomist/index.html',
        {'recommended': recommended})


def category(request, category_id, page_num=1):

    category_objects = Category.objects.get(id=category_id)

    objects = category_objects.objectproperty_set.order_by('id')

    context = {'category': category_objects}

    paginator = Paginator(objects, 6)

    try:
        context['objects'] = paginator.get_page(page_num)
    except PageNotAnInteger:
        context['objects'] = paginator.page(1)
    except EmptyPage:
        context['objects'] = paginator.page(paginator.num_pages)

    return render(request, 'neruhomist/objects.html', context)


def object(request, object_id):

    obj = ObjectProperty.objects.get(id=object_id)
    q = Q(object_type=obj.object_type) & Q(rooms=obj.rooms) & Q(category_object=obj.category_object) & ~Q(pk=obj.id)
    context = dict()
    context['interested'] = ObjectProperty.objects.filter(q).distinct()
    context['images'] = obj.images.all()
    context['object'] = obj
    context['count'] = context['interested'].count()

    return render(request, 'neruhomist/object.html', context)


def page(request, page_id):
    p = Page.objects.get(id=page_id)
    context = dict()
    context['page'] = p
    return render(request, 'neruhomist/page.html', context)
