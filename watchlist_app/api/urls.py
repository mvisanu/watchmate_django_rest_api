from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from watchlist_app.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV, StreamPlatformAV, 
                                     StreamPlatformDetailAV, ReviewList, ReviewDetail, 
                                     ReviewCreate, StreamPlatformVS, UserReview, WatchListGV)
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='StreamPlatform')

urlpatterns = [
    path('watchlist/', WatchListAV.as_view(), name='watchlist'),
    path('watchlist/<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'),
    path('search-list/', WatchListGV.as_view(), name='watchlist'),
   # path('list/', WatchListAV.as_view(), name='watchlist'),
   # path('<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail'),
   
   path('', include(router.urls)),
   
   path('stream/', StreamPlatformAV.as_view(), name='stream'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
  
   
   #path('review/', ReviewList.as_view(), name='review-list'), 
   #path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
   
   # path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'), 
   # path('stream/<int:pk>/reviews/', ReviewList.as_view(), name='review-list'), 
   # path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
   
   path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'), 
   path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'), 
   path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
   
   #path('review/', ReviewAV.as_view(), name='review'),
   #path('review/<int:pk>', ReviewDetailAV.as_view(), name='review-detail'),
   
#    path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
   path('reviews/', UserReview.as_view(), name='user-review-detail'),
]
