from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwner 
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter ,OrderingFilter
from .filters import PostFilter ,CommentFilter

class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['title', 'description']
    ordering_fields = ['create_at', 'update_at']
    ordering = ['-create_at']
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class =
    
    def perform_create(self, serializer):
        profile = self.request.user.profile 
        serializer.save(author=profile)

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner] 

class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['comment']
    ordering_fields = ['create_at', 'update_at']
    ordering = ['-create_at']
    filterset_class = CommentFilter
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk']) 
    
    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(
            author=profile,
            post_id=self.kwargs['post_pk']
        )

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    
    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        
        return Comment.objects.filter(post_id=post_id)