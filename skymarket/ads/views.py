from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from django.core.exceptions import ValidationError


from skymarket.ads.models import Ad, Comment
from skymarket.ads.permissions import AdUpdatePermission, CommentUpdatePermission
from skymarket.ads.serializers import AdDetailSerializer, AdDeleteSerializer, AdSerializer, CommentSerializer, \
    CommentDetailSerializer, CommentListSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


def root(request):
    return JsonResponse({"status": "ok"})


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def get(self, request, *args, **kwargs):
        ad_author = request.GET.get("author", None)
        if ad_author:
            self.queryset = self.queryset.filter(
                name__contains=ad_author
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get(self, request, *args, **kwargs):
        selection_name = request.GET.get("name", None)
        if selection_name:
            self.queryset = self.queryset.filter(
                name__contains=selection_name
            )

        return super().get(request, *args, **kwargs)


class CommentRetrieveView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentUpdatePermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentUpdatePermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get["image", None]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "title": self.object.title,
            "author": self.object.author.first_name,
            "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "created_at": self.object.created_at,
            "image": self.object.image.url if self.object.image else None,
        })
