from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .utils import DataMixin


class Theory(DataMixin, ListView):
    model = TheoryPost
    paginate_by = 13
    template_name = 'theory/theory.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**c_def, **context}

    def get_queryset(self):
        return TheoryPost.objects.all().order_by('-pk')


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'theory/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**c_def, **context}

    def get_success_url(self):
        return reverse('theory')


def user_logout(request):
    logout(request)
    return redirect('login')


class AddTheory(CreateView):
    template_name = 'theory/addTheory.html'
    fields = ('article', 'content')
    model = TheoryPost

    def post(self, request, *args, **kwargs):
        res = self.request.POST
        post = TheoryPost(
            article=res['article'],
            content=res['content'],
            author=self.request.user
        )
        post.save()
        return redirect('postTheory', post_id=post.pk)


class PostTheoryView(DataMixin, DetailView):
    template_name = 'theory/theoryPost.html'
    pk_url_kwarg = 'post_id'
    model = TheoryPost
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**c_def, **context}

    def get_object(self, queryset=None):
        obj = super(PostTheoryView, self).get_object()
        obj.count_view += 1
        obj.save()
        return super(PostTheoryView, self).get_object()


class EditPostTheory(DataMixin, UpdateView):
    model = TheoryPost
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    template_name = 'theory/editPost.html'
    fields = ('article', 'content')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**c_def, **context}


def delete_post(request, post_id):
    post = TheoryPost.objects.get(id=post_id)
    post.delete()
    return redirect('theory')