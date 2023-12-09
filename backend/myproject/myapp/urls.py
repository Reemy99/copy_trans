# from . import views
# from django.urls import path

# from .views import landing_page, redirect_to_intra_auth, intra_callback


# urlpatterns = [
#     # path('', views.index, name='index'),
#     # path('hello/', views.hello, name='hello'),
#     path('', landing_page, name='landing_page'),
#     path('redirect_to_intra_auth/', redirect_to_intra_auth, name='redirect_to_intra_auth'),
#     path('intra_callback/', intra_callback, name='intra_callback'),
#     # path('intra_login/', intra_login, name='intra_login'),
# ]

# from .views import intra_login


from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('redirect_to_intra_auth/', views.redirect_to_intra_auth, name='redirect_to_intra_auth'),
    path('intra_callback/', views.intra_callback, name='intra_callback'),
    path('intra_login/', views.intra_login, name='intra_login'),
    path('intra.html', views.intra_html, name='intra_html'),
    path('register/', views.register, name='register'),
    path('game-options/', views.game_options, name='game_options'),

    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]

# myapp/urls.py

from django.urls import path
from .views import redirect_to_intra_auth, intra_callback

urlpatterns = [
    path('redirect_to_intra_auth/', redirect_to_intra_auth, name='redirect_to_intra_auth'),
    path('intra_callback/', intra_callback, name='intra_callback'),
    # ... other app-specific URL patterns ...
]
