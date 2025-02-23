from django.views.generic import ListView, DetailView
from .models import Course, Module
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 9


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.modules.all().prefetch_related('videos', 'pdf_notes')
        return context
    
    
# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'courses/course_detail.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['modules'] = self.object.modules.all().prefetch_related('videos', 'pdf_notes')
#         return context