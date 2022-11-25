from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Comment
from ads.permissions import IsOwnerAdOrStaff
from ads.serializers import CommentSerializer, CommentDetailSerializer, CommentListSerializer, CommentCreateSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.order_by('-id')
    default_serializer = CommentSerializer
    serializer_classes = {
        'retrieve': CommentDetailSerializer,
        'list': CommentListSerializer,
        'create': CommentCreateSerializer
    }

    default_permission = [AllowAny()]
    permissions = {
        'create': [IsAuthenticated()],
        'retrieve': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'update': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'partial_update': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'destroy': [IsAuthenticated(), IsOwnerAdOrStaff()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
