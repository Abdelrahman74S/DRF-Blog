from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import Profile
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 

        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key  
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(ObtainAuthToken):
      def post(self,request, *args, **kwargs):
            response = super().post(request, *args, **kwargs)
            token = Token.objects.get(key=response.data['token'])
            return Response({
              'token': token.key,
              'user_id': token.user.id,
              'username': token.user.username
            })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        if request.auth:
            request.auth.delete() 
            
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK) 
        else:
            # هذا الـ Block لا يجب أن يتم الوصول إليه إذا كانت الصلاحية IsAuthenticated
            return Response({"detail": "No active token provided."}, status=status.HTTP_401_UNAUTHORIZED)
