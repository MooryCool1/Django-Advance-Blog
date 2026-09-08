from django.urls import include, path
from .views import indexView
from . import views
from django.views.generic import TemplateView
app_name = 'blog'
urlpatterns = [
    #path('fbv-index', views.indexView, name="fbv-index"),
    # path('cbv-index', TemplateView.as_view(template_name="index.html", extra_context={"name": "ali"})),
    path('post/', views.PostListView.as_view(), name='post-list'),
    #path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('post<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),

]   