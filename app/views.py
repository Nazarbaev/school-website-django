from django.views.generic import TemplateView, ListView

from app.models import Home, Gallery, GalleryCategory


class IndexView(ListView):
    model = Home
    template_name = "index.html"
    context_object_name = "home_list"


class GalleryView(ListView):
    model = Gallery
    template_name = "gallery.html"
    context_object_name = "gallery_images"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = GalleryCategory.objects.all()
        return context


class StarterPageView(TemplateView):
    template_name = "starter-page.html"


class BlogView(TemplateView):
    template_name = "blog.html"


class BlogDetailsView(TemplateView):
    template_name = "blog-details.html"


class CambridgeView(TemplateView):
    template_name = "cambridge.html"


class EdupageView(TemplateView):
    template_name = "edupage.html"


class FaqView(TemplateView):
    template_name = "FAQ.html"


class AchievementsView(TemplateView):
    template_name = "achievements.html"


class AchievementsDetailsView(TemplateView):
    template_name = "achievements-details.html"
