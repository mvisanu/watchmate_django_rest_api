from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
        #exclude = ['active']
        #fields = ['id', 'name', 'description']
        
        
    def get_len_name(self, objects):
        return len(object.name)
        
        
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name cannot be equal to description")
        return data
    
    def validate_name(self, value): 
        """ 
        field level validation
        """              
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

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