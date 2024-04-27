from django.urls import path
from .views import ArticlesList, ArticlesDetail, ArticlesCreate, ArticlesEdit, ArticlesDelete

urlpatterns = [
    path('', ArticlesList.as_view()),
    path('<int:pk>/', ArticlesDetail.as_view()),
    path('create/', ArticlesCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
    path('<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),




]