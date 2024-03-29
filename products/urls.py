from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.ProductListView.as_view()),
    # path('products-fbv/',views.product_list_view),
    # path('products/<int:pk>/',views.ProductDetailView.as_view()),
    path('products/<slug>/',views.ProductDetailSlugView.as_view()),
    # path('products-fbv/<int:pk>/',views.product_detail_view),
    # path('featured/',views.ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/',views.ProductFeaturedDetailView.as_view()),
]