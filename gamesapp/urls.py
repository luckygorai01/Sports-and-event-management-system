from django.urls import path
from . import views
urlpatterns=[
path('',views.function1, name="index"),
path('index',views.function6, name="home"),
path('matches/',views.function2, name="matches"),
path('players/',views.function3, name="players"),
path('blog/',views.function4, name="blog"),
path('contact/',views.function5, name="contact"),
path('sign/',views.function7, name="sign"),
path('login/',views.login, name="login"),
path('register/', views.register, name="register"),
path('profile/', views.function8, name="profile"),
path('logout/', views.logout, name="logout"),
]