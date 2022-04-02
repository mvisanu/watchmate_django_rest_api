from django.urls import path, include
#from watchlist_app.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
   path('watchlist/', WatchListAV.as_view(), name='watchlist'),
   path('watchlist/<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'),
   path('stream/', StreamPlatformAV.as_view(), name='stream'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
   path('review/', ReviewList.as_view(), name='review-list'),
   path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
   
   # path('review/', ReviewAV.as_view(), name='review'),
   # path('review/<int:pk>', ReviewDetailAV.as_view(), name='review-detail')
     
]
