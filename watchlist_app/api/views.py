#RestFramework import
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

# App Import
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)
        

class ReviewList(generics.ListCreateAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class StreamPlatformVS(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)       
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):
    
    def get(self, request, pk):        
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListDetailAV(APIView):
    
    def get(self, request, pk):        
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
    


# class ReviewAV(APIView):
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ReviewDetailAV(APIView):
    
#     def get(self, request, pk):        
#         try:
#             review = Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ReviewSerializer(review, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request,pk):
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#     def delete(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)       
# Function view
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)