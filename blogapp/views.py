from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import blogdb
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = blogdb
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = blogdb
    template_name = 'post_detail.html'
    # context_object_name = 'indiv_post'
  

class BlogCreateView(CreateView):
    model = blogdb
    
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = blogdb
    template_name = 'post_edit.html'
    fields = ['title', 'body']    

class BlogDeleteView(DeleteView):
    model = blogdb
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



      

