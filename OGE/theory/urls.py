from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Theory.as_view(), name='theory'),
    path('logout/', user_logout, name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('addTheory/', AddTheory.as_view(), name='addTheory'),
    path('post/<int:post_id>/', PostTheoryView.as_view(), name='postTheory'),
    path('editPost/<int:post_id>/', EditPostTheory.as_view(), name='editPost'),
    path('deletePost/<int:post_id>', delete_post, name='deletePost')
]
