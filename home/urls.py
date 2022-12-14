from django.urls import path
from . import views
import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('n/register',views.register,name='register'),
    path("<str:username>", views.profile, name='profile'),
    path("n/following", views.following, name='following'),
    path("n/saved", views.saved, name="saved"),
    path('n/settings/',views.settings,name='settings'),
            path('password_reset/',auth_views.PasswordResetView.as_view(
        template_name = 'password_reset.html'
    ),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'password_reset_done.html'
    ),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(
        template_name = 'password_reset_confirm.html'
    ),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name = 'password_reset_complete.html'
    ),name='password_reset_complete'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
