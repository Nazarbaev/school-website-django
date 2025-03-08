from django.conf.urls.static import static
from stem import settings
from django.urls import path
from .views import (IndexView,
                    GalleryView,
                    StarterPageView,
                    BlogView,
                    BlogDetailsView,
                    CambridgeView,
                    EdupageView,
                    FaqView,
                    AchievementsView,
                    AchievementsDetailsView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("starter-page/", StarterPageView.as_view(), name="starter-page"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog-details/", BlogDetailsView.as_view(), name="blog-details"),
    path("cambridge/", CambridgeView.as_view(), name="cambridge"),
    path("edupage/", EdupageView.as_view(), name="edupage"),
    path("faq/", FaqView.as_view(), name="faq"),
    path("achievements/", AchievementsView.as_view(), name="achievements"),
    path("achievements-details/", AchievementsDetailsView.as_view(), name="achievements-details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
