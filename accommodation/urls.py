from django.urls import path


from . import views


urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('addPost', views.add_Post.as_view(),name="addPost"),
    path('detail/<int:id>', views.detail_view,name="detail"),
    path('edit/<int:pk>', views.update_Post.as_view(),name="edit"),
    path('login', views.login_user,name="login"),
    path('signup', views.signup,name="signup"),
    path('logout',views.logoutUser,name='logout'),
    #path('booking',views.book.as_view(),name='book'),
    path('post',views.post,name='post'),
    path('api',views.api,name='api'),
    path('api/house-list/',views.List,name='List'),

]