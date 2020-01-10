from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from serializer_api.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    # author = JournalistSerializer(read_only=True)
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__" # we want all the fields of our model
        # fields = ("title", "description", "body") # we want to choose a couple of fields!

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """ check that description and title are different
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data

    def validate_title(self, value):
        """ check that title is at least 30 chars long
        https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
        """
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long!")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="article-detail")

    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = '__all__'
