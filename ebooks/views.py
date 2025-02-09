from django.core.paginator import Paginator
from django.shortcuts import render
from .models import eBook, Tag

def ebook_list(request):
    ebooks = eBook.objects.all().order_by('-uploaded_at')
    
    # Filtering
    category = request.GET.get('category')
    search_query = request.GET.get('search')
    tags = request.GET.getlist('tags')
    
    if category:
        ebooks = ebooks.filter(category=category)
        
    if search_query:
        ebooks = ebooks.filter(title__icontains=search_query)
        
    if tags:
        ebooks = ebooks.filter(tags__slug__in=tags).distinct()
    
    # Pagination
    paginator = Paginator(ebooks, 9)  # Show 9 ebooks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        # 'categories': dict(eBook.category),
        'tags': Tag.objects.all(),
        'selected_tags': tags,
        'selected_category': category,
        'search_query': search_query or '',
    }
    return render(request, 'ebooks/ebook_list.html', context)