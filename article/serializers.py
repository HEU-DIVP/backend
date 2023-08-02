from rest_framework import serializers

from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    cid = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'cid', 'name'
        )

    def get_cid(self, obj):
        return obj.id


class ArticleSerializer(serializers.ModelSerializer):
    aid = serializers.SerializerMethodField()
    source = CategorySerializer()
    create_time = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Article
        fields = (
            'aid', 'title', 'source', 'url', 'click_count', 'create_time'
        )

    def get_aid(self, obj):
        return obj.id
