from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from salingbantu.models import *
from salingbantu.forms import *

# Create your views here.
class SalingBantu(ListView):
    model = Post
    template_name='home.html'

class DetailsPost(DetailView):
    model = Post
    template_name ='details_post.html'

class AddPost(CreateView):
    model = Post
    template_name ='add_post.html'
    fields = '__all__'

class AddComment(CreateView):
    model = Post
    form_class = FormComment
    template_name ='add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('salingbantu:salingbantu')

