from rest_framework import viewsets
from .models import Category, Comment, Post
from .serializers import CategorySerializer, CommentSerializer, PostSerializer
from rest_framework import permissions
from rest_framework import authentication


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
