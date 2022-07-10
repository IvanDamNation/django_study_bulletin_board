from django_filters import FilterSet
from board.models import Comment


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = ('news', )
