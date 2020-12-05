from django.contrib.auth.views import LoginView
from django.urls import path, include

from account.views import user_signup, user_profile, user_signout

urlpatterns = (
    # path('signin', LoginView.as_view(template_name='registration/signin.html'), name='signin'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>', user_profile, name='user profile'),
    path('signup/', user_signup, name='user signup'),
    path('signout/', user_signout, name='user signout')
)
