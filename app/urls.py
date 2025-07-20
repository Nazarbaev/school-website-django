from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (IndexView,
                    GalleryView,
                    StarterPageView,
                    BlogDetailsView,
                    CambridgeView,
                    EdupageView,
                    FaqView,
                    AchievementsDetailsView, blog_index, achievements_index, stats_index)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("starter-page/", StarterPageView.as_view(), name="starter-page"),
    path("blog/", blog_index, name="blog"),
    path('blog-details/<int:pk>/', BlogDetailsView.as_view(), name="blog-details"),
    path("cambridge/", CambridgeView.as_view(), name="cambridge"),
    path("edupage/", EdupageView.as_view(), name="edupage"),
    path("faq/", FaqView.as_view(), name="faq"),
    path("achievements/", achievements_index, name="achievements"),
    path('achievements-details/<int:pk>', AchievementsDetailsView.as_view(), name="achievements-details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
