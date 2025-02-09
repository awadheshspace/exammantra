from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import PDFNote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import Ebook, EbookCategory, Board
# from django.db.models import Q




def main_page(request):
    return render(request,'login/mainpage.html')



# def notes_list(request):
#     technical_notes = PDFNote.objects.filter(category='technical')
#     board_notes = PDFNote.objects.filter(category='board')
    
#     context = {
#         'technical_notes': technical_notes,
#         'board_notes': board_notes
#     }
#     return render(request, 'exammantrabihar/notes_list.html', context)

def notes_list(request):
    search_query = request.GET.get('q', '')
    tech_page = request.GET.get('tech_page', 1)
    board_page = request.GET.get('board_page', 1)
    
    # Base querysets
    technical_notes = PDFNote.objects.filter(category='technical')
    board_notes = PDFNote.objects.filter(category='board')
    
    # Apply search filter
    if search_query:
        technical_notes = technical_notes.filter(subject__icontains=search_query)
        board_notes = board_notes.filter(subject__icontains=search_query)
    
    # Pagination
    tech_paginator = Paginator(technical_notes, 6)  # 6 items per page
    board_paginator = Paginator(board_notes, 6)
    
    try:
        tech_notes = tech_paginator.page(tech_page)
    except (EmptyPage, PageNotAnInteger):
        tech_notes = tech_paginator.page(1)
        
    try:
        board_notes = board_paginator.page(board_page)
    except (EmptyPage, PageNotAnInteger):
        board_notes = board_paginator.page(1)

    context = {
        'tech_notes': tech_notes,
        'board_notes': board_notes,
        'search_query': search_query,
    }
    return render(request, 'exammantrabihar/notes_list.html', context)
# def index_page(request):
#     return render(request,'login/index.html')    


