from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from authapp import views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('signup', views.signup,name="signup"),
    path('login', views.handlelogin,name="handlelogin"),
    path('logout', views.handleLogout,name="handlelogout"),
    path('contact',views.contact,name="contact"),
    path('profile',views.profile,name="profile"),
    path('database', views.database, name = "database"),
    path('calendar/', views.calendar, name='calendar'),
    path('get_activities/', views.get_activities, name='get_activities'),
    path('bench_press/', views.bench_press,name="bench_press"),
    path('squat/', views.squat,name="squat"),
    path('barbell_row/', views.barbell_row,name="barbell_row"),


    # path('test', views.test, name = "test"),



    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]