from django.contrib.auth.views import *
from .views import *
from django.urls import path



urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

app_name='account'

urlpatterns += [
    path('',ArticleList.as_view(), name='home'),
    path('article/create',ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>',ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>',ArticleDelete.as_view(), name='article-delete'),
    path('profile/',Profile.as_view(), name='profile'),
]