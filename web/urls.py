
from django.urls import path
from . import views 
from .views import AddCommentForm, PostListView , PostDetailView,AddCommentForm , AddItemForm
urlpatterns = [
    path('contact/', views.contact, name='Booklary-contact'),
    path('', views.home, name='Booklary-index'),
    path('home/', views.home, name='Booklary-home'),
    path('library/', PostListView.as_view( ) , name='Booklary-library'),
    path('about/', views.about, name='Booklary-about'),
    path('library/<int:pk>/', PostDetailView.as_view( ) , name='post-detail'),
    path('library/<int:pk>/comment/', AddCommentForm.as_view( ), name='add-comment' ),
    path('library/<int:pk>/added/', AddItemForm.as_view() , name='item-added' )

]