from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    path('',views.index,name='index'),
    path('rules/',views.rules,name='rules'),
    path('quiz/<str:title>/',views.paginated_quiz,name='paginated_quiz'),
    path('mock/<int:post_id>/',views.quiz,name='quiz'),
    path('search/',views.search,name='search'),
]
