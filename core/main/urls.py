from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('signup/', views.signup_view, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:category_id>/events/', views.category_events, name='category_events'),
    path('category/<int:category_id>/bookings/', views.category_bookings, name='category_bookings'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),
    path('search/', views.search_events, name='search_events'),
    path('success/', views.success_page, name='success_page'),
    path('user/profile/edit/', views.profile_edit, name='profile_edit'),
]