from django.urls import path, include
#from watchlist_app.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
   path('list/', WatchListAV.as_view(), name='watchlist'),
   path('list/<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'),
   path('stream/', StreamPlatformAV.as_view(), name='stream'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
   #path('list/', movie_list, name='movie-list'),
   #path('<int:pk>', movie_details, name='movie-detail'),
   
]
