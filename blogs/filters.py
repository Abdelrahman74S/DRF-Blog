import django_filters

from .models import Post, Comment

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    author_name = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Post
        fields = ['title', 'description','author_name']
        
class CommentFilter(django_filters.FilterSet):
    comment = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains',field_name='author__user__username',)

    class Meta:
        model = Comment
        fields = ['comment']