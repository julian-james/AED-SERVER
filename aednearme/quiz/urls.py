from django.urls import path
from . import views

urlpatterns = [
    path('<category>/', views.get_quiz_questions),
    # path('/', views.create_)
]