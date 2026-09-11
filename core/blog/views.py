from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
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

class PostListView(ListView):
    #model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-created_date']
    queryset = Post.objects.all()
    #def get_queryset(self):
    #    posts = Post.objects.filter(status=True)
    #    return posts

class PostDetailView(DetailView):
    model = Post

#class PostCreateView(FormView):
#    template_name = 'blog/contact.html'
#    form_class = PostForm   
#    success_url = '/blog/post/'   
#
#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    #fields = ['author','title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'