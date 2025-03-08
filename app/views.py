from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class GalleryView(TemplateView):
    template_name = "gallery.html"


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
