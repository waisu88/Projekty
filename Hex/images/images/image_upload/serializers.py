from rest_framework import serializers
from .models import Image, Thumbnail, BinaryImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by']  
  

class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = '__all__'


# class ExpiringLinkSerializer(serializers.ModelSerializer):
#     # # base_image = serializers.RelatedField(source='image', read_only=True)
#     # created_by_data = serializers.SerializerMethodField(read_only=True)


#     class Meta:
#         model = ExpiringLink
#         fields = ['seconds_to_expiration', 'created']
#         excluded = ['expiring_link_2', 'created_by', 'base_image', 'expiration_date']
#         # excluded = ['base_image']


class BinaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinaryImage
        fields = ['seconds_to_expiration', 'binary_image']
        excluded = ['created_by', 'base_image', 'expiration_date','created']

