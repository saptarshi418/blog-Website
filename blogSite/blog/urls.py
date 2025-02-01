
from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index , name='home'),
    path('createblog/', views.create_blog , name='create'),
    path('<int:blog_id>/edit/', views.blog_edit , name='edit'),
    path('<int:blog_id>/delete/', views.blog_delete , name='delete'),
    path('<int:blog_id>/', views.blog_view , name='blog_detail'),
    path('accounts/register/',views.register , name = 'register'),
    path('accounts/login/',views.login_view , name = 'login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]



# path('blog/<int:blog_id>/',views.blog_view , name = 'detailed_view')