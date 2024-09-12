from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import PostUpdateForm,CommentForm
from blog.models import post,category
from django.http import HttpResponseRedirect
from django.views import View

class PostList(ListView):
    model = post
    context_object_name = "post"
    template_name = "post_list.html"

    def get_queryset(self):
        
        queryset = self.model.objects.all()
        if self.request.GET.get('category'):
            try:
                queryset = self.model.objects.filter(category__in=self.request.GET.getlist('category')).distinct()
            except:
                pass
        return queryset
    def get_context_data(self,**kwargs):
        context = super(PostList,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['category'] = category.objects.all()
        return context

class PostDetail(LoginRequiredMixin,DetailView):
    model = post
    template_name = "post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['user'] = self.request.user
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            print(self.object.pk)
            return redirect('blog:detail-post', pk=self.object.pk)

        else:
            return self.get(request, *args, **kwargs)


class PostCreate(LoginRequiredMixin, CreateView):
    model = post
    fields = ["title", "content","category"]
    success_url = reverse_lazy("blog:list-post")
    context_object_name = "posts"
    template_name = "post_create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = post
    form_class = PostUpdateForm
    template_name = "post_update.html"
    # template_name_suffix = "_update"
    success_url = reverse_lazy("blog:list-post")
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = category.objects.all()
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = post
    success_url = reverse_lazy("blog:list-post")
    template_name = "post_confirm_delete.html"
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)



