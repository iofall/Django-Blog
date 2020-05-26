from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blog import models, forms

class AboutView(TemplateView):
    template_name = 'about.html'

class HelpView(TemplateView):
    template_name = 'help.html'

class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context

class PostDetailView(DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = models.Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = models.Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__isnull=True).order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context

def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

####### Comment Views ###########

def add_comment_to_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
