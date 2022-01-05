from django.urls import path
from .views.users import SignUp, SignIn,SignOut,ChangePassword
from .views.ideas import IdeasView,IdeaView

urlpatterns = [
    path('api/auth/signup/', SignUp.as_view(), name='sign-up'),
    path('api/auth/signin/', SignIn.as_view(), name='sign-in'),
    path('api/auth/signout/', SignOut.as_view(), name='sign-out'),
    path('api/auth/change-password/', ChangePassword.as_view(), name='change-password'),
    path('ideas/', IdeasView.as_view(), name='ideas'),
    path('idea/<int:pk>/', IdeaView.as_view(), name='idea'),
]