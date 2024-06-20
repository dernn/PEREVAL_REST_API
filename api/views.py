from api.models import Coords, Images, Level, Pereval, Users
from api.serializers import CoordsSerializer, ImagesSerializer, LevelSerializer, PerevalSerializer, UsersSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ['user__email']
    http_method_names = ['get', 'post', 'patch']

    # POST-method submitData
    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data,
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error',
                'id': None,
            })

    # PATCH-method submitData
    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Entry successfully modified',
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors["non_field_errors"][0]
                })
        else:
            return Response({
                'state': '0',
                'message': f'Rejected: object status "{pereval.get_status_display()}"'
                # status must be "new"
            })

    def paginate_queryset(self, queryset):
        """
        If you pass parameter '?get_all=true' when making the request, response will be without pagination.
        """
        if self.request.query_params.get('get_all', False) == 'true':
            return None
        return super().paginate_queryset(queryset)
