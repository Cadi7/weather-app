from drf_util.decorators import serialize_decorator
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
import geocoder
from apps.users.models import User
from apps.users.serializers import RegisterSerializer, UserSerializer, LoginSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return UserSerializer
        return super().get_serializer_class()

    @serialize_decorator(RegisterSerializer)
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        user = User.objects.create(
            first_name=request.valid['first_name'],
            last_name=request.valid['last_name'],
            username=request.valid['email'],
            email=request.valid['email'],
        )

        location = geocoder.ip('me')
        user.location = location.city
        user.set_password(request.valid['password'])
        user.save()
        return Response(status=status.HTTP_201_CREATED, data=UserSerializer(user).data)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny], serializer_class=LoginSerializer)
    def login(self, request):
        user = get_object_or_404(User, email=request.data['email'])

        if not user.check_password(request.data['password']):
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(self.get_tokens_for_user(user))
