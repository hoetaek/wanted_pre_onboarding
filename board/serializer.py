from rest_framework import serializers
from .models import Post, Company

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['company', 'position', 'payment', 'description', 'technology']


class PostListSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'company', 'country', 'area', 'position', 'payment', 'technology']

    def get_company(self, obj):
        return str(obj.company)

    def get_country(self, obj):
        return obj.company.country

    def get_area(self, obj):
        return obj.company.area

class PostDetailSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    other_posts = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'company', 'country', 'area', 'position',
                  'payment', 'description', 'technology', 'other_posts']

    def get_company(self, obj):
        return str(obj.company)

    def get_country(self, obj):
        return obj.company.country

    def get_area(self, obj):
        return obj.company.area

    def get_other_posts(self, obj):
        return obj.company.post_set.values_list('id', flat=True)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
