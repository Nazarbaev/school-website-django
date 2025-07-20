from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from app.models import Home, GalleryCategory, GalleryImage,BlogPost,BlogCategory,Stats,TeamMember,FAQ
from django.core.paginator import Paginator

class IndexView(ListView):
    model = Home
    template_name = "index.html"
    context_object_name = "home_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = Stats.objects.last()
        context['blogs'] = BlogPost.objects.order_by('-created_at')[:3]
        context['teachers'] = TeamMember.objects.order_by('-created_at')[:6]
        return context



class GalleryView(ListView):
    template_name = 'gallery.html'
    paginate_by = 9

    def get_queryset(self):
        category_name = self.request.GET.get('category')

        images = GalleryImage.objects.select_related('gallery__category').all()

        if category_name:
            images = images.filter(gallery__category__title__iexact=category_name)

        # Order by gallery creation date desc, then image id desc
        images = images.order_by('-gallery__created_at', '-id')

        return images

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context

class StarterPageView(TemplateView):
    template_name = "starter-page.html"


def blog_index(request):
    all_posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})

def stats_index(request):
    stats =   Stats.objects.last()
    return render(request,'index.html', {'stats': stats})

class BlogDetailsView(DetailView):
    model = BlogPost
    template_name = "blog-details.html"
    context_object_name = "post"


def achievements_index(request):
    try:
        category = BlogCategory.objects.get(name='Достижения')
        all_posts = BlogPost.objects.filter(category=category).order_by('-created_at')
    except BlogCategory.DoesNotExist:
        all_posts = BlogPost.objects.none()  # Empty QuerySet

    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'achievements.html', {'page_obj': page_obj})


class AchievementsDetailsView(DetailView):
    model = BlogPost
    template_name = "achievements-details.html"
    context_object_name = "post"

class CambridgeView(TemplateView):
    template_name = "cambridge.html"


class EdupageView(TemplateView):
    template_name = "edupage.html"



class FaqView(ListView):
    model = FAQ
    template_name = "FAQ.html"
    context_object_name = "faqs"  # optional but recommended

    def get_queryset(self):
        return FAQ.objects.order_by('-created_at')[:10]



