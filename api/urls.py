from django.urls import path, include

# from .views import article_list, article_detail
# from .views import ArticleList, ArticleDetail
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="articles")
urlpatterns = [
    # path("articles", ArticleList.as_view()),
    # path("articles/<int:id>", ArticleDetail.as_view()),
    path("", include(router.urls))
]
