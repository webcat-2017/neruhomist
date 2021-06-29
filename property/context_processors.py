from .models import Setting, Category, Page

def settings(request):

    settings = Setting().getSettings()

    categories = Category.objects.order_by('id')
    pages = Page.objects.filter(status=True)

    return {'categories': categories, 'settings': settings, 'base_url': settings.base_url, 'pages': pages}
