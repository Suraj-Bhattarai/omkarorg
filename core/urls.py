from django.urls import path
from core import views



urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path("product/<slug>/", views.ProductView.as_view(),name="product"),
    path("category/<slug>/", views.CategoryView.as_view(),name="category"),
    path("pos_products/", views.PosProduct.as_view(), name="pos-products"),
    path("it_products/", views.ItProduct.as_view(), name="it-products"),  


    path("addproduct/", views.AddProduct.as_view(), name="addproduct"),
    path("product/edit/<slug>/", views.ProductUpdateView.as_view(), name="update-product"),
    path("product/<slug>/remove", views.ProductDeleteView.as_view(), name="remove"),


    path("about/", views.AboutView.as_view(), name="about"),
    path("search/", views.SearchView.as_view(), name="search"),


    #Contact_us
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),


    path("service/", views.AddService.as_view(), name="addservice"),
    path("track_service/", views.TrackService.as_view(), name="track-service"),
    path("service/edit/<slug>/", views.ServiceUpdateView.as_view(), name="update-service"),
    path("service/<str:slug>/remove", views.service_delete , name="remove_service"),
]