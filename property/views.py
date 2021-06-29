from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render
from django.db.models import Q
from .models import *


def index(request):

    recommended = ObjectProperty.objects.filter(recommended = True)

    return render(request, 'neruhomist/index.html', {'recommended': recommended,})


def category(request,category_id, page_num = 1):

    context = {}

    category = Category.objects.get(id = category_id)

    objects = category.objectproperty_set.order_by('id')

    context['category'] = category

    paginator = Paginator(objects, 6)

    #page_num = request.GET.get('page')

    try:
        context['objects'] = paginator.get_page(page_num)
    except PageNotAnInteger:
        context['objects'] = paginator.page(1)
    except EmptyPage:
        context['objects'] = paginator.page(paginator.num_pages)

    return render(request, 'neruhomist/objects.html', context)


def object(request, object_id):
    context = {}

    object = ObjectProperty.objects.get(id=object_id)

    #interested = ObjectProperty.objects.filter(object_type = object.object_type, locality = object.locality, price__gte = object.price)

    q = Q(object_type = object.object_type) & Q(rooms = object.rooms) & Q(category_object = object.category_object) & ~Q(pk = object.id)
    context['interested'] = ObjectProperty.objects.filter(q).distinct()
    context['images'] = object.images.all()
    context['object'] = object
    context['count'] = context['interested'].count()

    return render(request, 'neruhomist/object.html', context)

def page(request, page_id):
    context = {}

    page = Page.objects.get(id=page_id)

    context[''] = ObjectProperty.objects.filter().distinct()
    context['image'] = page.image.all()
    context['page'] = page


    return render(request, 'neruhomist/object.html', context)

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("page error- no found")

    latest_comment_list = a.comment_set.order_by('-id')[:4]
    return render(request, 'articles/show.html',{'article':a, 'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("page error- no found")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('articles:show', args= (a.id,)))
