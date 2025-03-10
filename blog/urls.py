from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

urlpatterns=[
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',views.UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',views.DeletePostView.as_view(),name='post_remove'),
    
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
    path('accounts/login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page=reverse_lazy('post_list')),name='logout'),

    

]