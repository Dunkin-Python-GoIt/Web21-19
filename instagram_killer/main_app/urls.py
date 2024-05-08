from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    # path("post/", views.post, name="post"),
    # path("post/<int:post_id>/", views.post_details, name="post_details"),
    path("post/", views.PostCreateView.as_view(), name="post"),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
    path("register/", views.register, name="register"), 
]
