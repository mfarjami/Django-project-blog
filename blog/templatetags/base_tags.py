from blog.models import *
from django import template
from django.db.models import *
from datetime import *

register = template.Library()


@register.inclusion_tag('blog/partials/category_nav.html')
def category_navbar():
   return {
      'category' : Category.objects.filter(status=True)
   }

@register.inclusion_tag('blog/partials/sidebar.html')
def popular_articles():
   last_month = datetime.today() - timedelta(days=30)
   return {
      'articles' : Article.objects.published().annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5],
      'title':'Most visited articles of the month'
   }

@register.inclusion_tag('blog/partials/sidebar.html')
def hot_articles():
   last_month = datetime.today() - timedelta(days=30)
   return {
      'articles' : Article.objects.published().annotate(count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=7))).order_by('-count', '-publish')[:5],
      'title':'Hot articles of the month'
   }


@register.inclusion_tag('registration/partials/link.html')
def link(request, link_name, content, classes):
   return {
      "request": request,
      "link_name": link_name,
      "link": f"account:{link_name}",
      "content": content,
      "classes": classes,
   }