from .models import Category

def categories_context(request):
    categories = Category.objects.prefetch_related(
        'subcategories',
        'subcategories__series'
    ).all()
    return {'categories': categories}
