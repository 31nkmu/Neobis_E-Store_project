from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from applications.account import serializers

User = get_user_model()


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class ActivationApiView(ListAPIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save(update_fields=['is_active', 'activation_code'])
            return Response({'msg': 'ваш аккаунт успешно активирован'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'некоректный код активации'})


class ChangePasswordApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]


class ForgotPasswordApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordSerializer


class ForgotPasswordConfirmApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordConfirmSerializer
