from django.urls import path
from .views import LinksView , LinkDetailView , UserLinksView , DownloadLinkView

urlpatterns = [
    path('' , LinksView.as_view() ),
    path('file/<str:url>/' , LinkDetailView.as_view() , name='file'),
    path('my-links/' , UserLinksView.as_view() , name='my-links'),
    path('download/<str:url>/', DownloadLinkView.as_view(), name='download_link'),

]