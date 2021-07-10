from .models import *

def settings(request):

    context = dict()

    settings = Setting().getSettings()

    categories = Category.objects.order_by('id')
    pages = Page.objects.filter(status=True)

    object_type = ObjectProperty.object_type
    context['categories'] = categories
    context['settings'] = settings
    context['base_url'] = settings.base_url
    context['pages'] = pages
    context['object_type'] = (
            'Квартира',
            'Будинок',
            'Земельна ділянка',
            'Дачний масив',
            'Комерційна нерухомість')
    return context
