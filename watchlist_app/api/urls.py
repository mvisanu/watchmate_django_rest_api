from django.urls import path, include
#from watchlist_app.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
   path('watchlist/', WatchListAV.as_view(), name='watchlist'),
   path('watchlist/<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'),
   path('stream/', StreamPlatformAV.as_view(), name='stream'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail')
     
]
