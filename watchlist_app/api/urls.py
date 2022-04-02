from django.urls import path, include
#from watchlist_app.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewAV, ReviewDetailAV

urlpatterns = [
   path('watchlist/', WatchListAV.as_view(), name='watchlist'),
   path('watchlist/<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'),
   path('stream/', StreamPlatformAV.as_view(), name='stream'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
   path('review/', ReviewAV.as_view(), name='review'),
   path('review/<int:pk>', ReviewDetailAV.as_view(), name='review-detail')
     
]
