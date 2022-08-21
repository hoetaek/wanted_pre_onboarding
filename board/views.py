from rest_framework.viewsets import ModelViewSet
from .serializer import CompanySerializer, PostCreateUpdateSerializer, PostListSerializer, PostDetailSerializer
from .models import Post, Company

# Create your views here.
class PostViewset(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostCreateUpdateSerializer  # I dont' know what you want for create/destroy/update.


class CompanyViewset(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
