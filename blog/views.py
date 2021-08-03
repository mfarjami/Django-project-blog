from django.shortcuts import render, get_object_or_404
from account.models import User
from django.views.generic import *
from .models import *
from account.mixins import *
from django.db.models import *

# Create your views here.
class ArticleList(ListView):
    queryset = Article.objects.published()[:4]



class ArticleAllList(ListView):
    queryset = Article.objects.published()
    template_name = "blog/Article_blog.html"
    paginate_by = 6

class ArticleDetail(DeleteView):
    template_name = 'blog/Article_detail.html'
    def get_object(self):
        slug =  self.kwargs.get('slug')
        article =  get_object_or_404(Article.objects.published(), slug=slug)

        ip_address = self.request.user.ip_address
        if article not in ip_address.hits.all():
            article.hits.add(ip_address)

        return article

class ArticlePreview(AuthorAccessMixin, DeleteView):
    template_name = 'blog/Article_detail.html'
    def get_object(self):
        pk =  self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


    
class CategoryList(ListView):
    paginate_by = 4
    template_name = "blog/category_list.html"

    def get_queryset(self):
        global category
        slug =  self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by = 1
    template_name = "blog/author_list.html"

    def get_queryset(self):
        global author
        username =  self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context

class SearchList(ListView):
	template_name = 'blog/search_list.html'

	def get_queryset(self):
		search = self.request.GET.get('q')
		return Article.objects.filter(Q(body__icontains=search) | Q(title__icontains=search) | Q(snippet__icontains=search))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')
		return context
