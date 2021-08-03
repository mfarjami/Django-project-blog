from django.urls import path, re_path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('all/', ArticleAllList.as_view(), name='all-posts'),
    # path('all/page/<int:page>', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('preview/<int:pk>', ArticlePreview.as_view(), name='preview'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/', AuthorList.as_view(), name='author'),
    path('search/', SearchList.as_view(), name='search'),
]