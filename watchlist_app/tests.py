from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="test1", password="Password@123")
        self.token = Token.objects.get(user__username="test1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                                           about="#1 Platform", 
                                                           website="http://www.netflix.com")
    
    def test_watchlist_create_normaluser(self):
        
        data = {
            "name": "Netflix",
            "about": "#1 Streaming platform",
            "website": "http://www.netflix.com"
        }
        
        url = reverse('streamplatform-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        url = reverse('streamplatform-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_id(self):
        url = reverse('streamplatform-detail', args=(self.stream.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="test1", password="Password@123")
        self.token = Token.objects.get(user__username="test1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                                           about="#1 Platform", 
                                                           website="http://www.netflix.com")
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                         storyline="sample movie", active=True)
    
    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "Example Movie",
            "storyline": "Example story",
            "active": True,
        }
        
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_id(self):
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')
        self.assertEqual(models.WatchList.objects.count(), 1)
        
        
class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="test1", password="Password@123")
        self.token = Token.objects.get(user__username="test1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                                           about="#1 Platform", 
                                                           website="http://www.netflix.com")
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                          storyline="sample movie", active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example Movie2",
                                                          storyline="sample movie", active=True)
        
        self.review = models.Review.objects.create(review_user=self.user, 
                                                   rating=5, 
                                                   comment="Great Movie",                                                    
                                                   active=True, 
                                                   watchlist_id=self.watchlist2.id)
        
    def test_review_create(self):
        
        data = {
           "review_user": self.user.id,
            "rating": 5,
            "comment": "Greate Movie!",                      
            "active": True
              
        }
        
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(models.Review.objects.count(), 1)       
        #self.assertEqual(models.Review.objects.get().rating, 5)
        
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        
        
    def test_review_create_anonymous(self):
        data = {
           "review_user": self.user.id,
            "rating": 5,
            "comment": "Greate Movie!",                      
            "active": True            
        }
        
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_update(self):
        data = {
           "review_user": self.user.id,
            "rating": 4,
            "comment": "Updated a Movie!",                            
            "active": False,
            "watchlist_id": self.watchlist2.id                  
        }
        
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_id(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    #test with query string
    def test_review_user(self):
        response = self.client.get('/api/reviews/?useranme' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        