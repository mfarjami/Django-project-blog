from blog.models import *
from django import template
from django.db.models import *
from datetime import *

register = template.Library()

@register.inclusion_tag('blog/partials/popular_articles.html')
def popular_articles():
   last_month = datetime.today() - timedelta(days=30)
   return {
      'popular_articles' : Article.objects.published().annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5]
   }

@register.inclusion_tag('blog/partials/category_nav.html')
def category_navbar():
   return {
      'category' : Category.objects.filter(status=True)
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