from django.urls import path
from . import views
# URL conf
urlpatterns =[ 
    path("", views.say_hello, name='index'),
    path('delete/<int:post_id>/',views.delete, name='delete'),
    path('edit/<int:post_id>/',views.edit, name='edit'),
    path('like/<int:post_id>/',views.like,name='like'),
]