from rest_framework.viewsets import ModelViewSet
from .serializer import CompanySerializer, PostCreateUpdateSerializer, PostListSerializer, PostDetailSerializer
from .models import Post, Company
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action

# Create your views here.
class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['technology', 'company__name', 'position']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostCreateUpdateSerializer

class CompanyViewset(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
