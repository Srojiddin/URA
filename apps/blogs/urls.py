from django.urls import path
from .views import (BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView,DepartmentsListView, AboutUsView,GalleryListView,ContactListView,
                    GallerySingleView, BlogLargeView,BlogSingleView, GalleryUpdateView, GalleryDeleteView, GalleryCreateView,NewssearchView)



urlpatterns = [
    path('create/blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('blog//delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('departments/', DepartmentsListView.as_view(), name='departments'),
    path('about/',  AboutUsView.as_view(), name='about_us'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/single', GallerySingleView.as_view(), name='gallery_detail'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('blog/large', BlogLargeView.as_view(), name='blog-large'),
    path('blog/single', BlogSingleView.as_view(), name='blog-single'),
    path('gallery/<int:pk>/update/', GalleryUpdateView.as_view(), name='gallery_update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete'),
    path('gallery/create/', GalleryCreateView.as_view(), name='gallery_list'),
    path('news/search/', NewssearchView.as_view(), name='news_earch'),
]

