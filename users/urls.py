from django.urls import path
from users.views import login, profile, registration, logout

app_name = 'products'
urlpatterns = [

    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

]
