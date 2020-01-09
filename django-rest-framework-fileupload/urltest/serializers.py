from rest_framework import serializers

from urltest.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return obj.img.url

    class Meta:
        model = ImageModel
        fields = '__all__'
