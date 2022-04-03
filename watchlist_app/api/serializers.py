from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"
        
class WatchListSerializer(serializers.ModelSerializer):   
    #review = ReviewSerializer(many=True, read_only=True)
    #platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = WatchList
        fields = "__all__"
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):   
    watchlist = WatchListSerializer(many=True, read_only=True)  
     
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

    
     

# def name_length(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name cannot be equal to description")
#         return data
    
    # def validate_name(self, value): 
    #     """ 
    #     field level validation
    #     """              
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value