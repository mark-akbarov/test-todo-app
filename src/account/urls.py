from django.urls import path


from account.views.login import LoginAPIView
from account.views.signup import SignupAPIView


urlpatterns = [    
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
