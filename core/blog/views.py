from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

def indexView(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context 

class PostListView(LoginRequiredMixin,ListView):
    #model = Post
    permission_required = 'blog.view_post'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-created_date']
    queryset = Post.objects.all()
    #def get_queryset(self):
    #    posts = Post.objects.filter(status=True)
    #    return posts

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

#class PostCreateView(FormView):
#    template_name = 'blog/contact.html'
#    form_class = PostForm   
#    success_url = '/blog/post/'   
#
#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #fields = ['author','title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'