from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.response import Response

class LoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            data = serializer.data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # token, created = Token.objects.get_or_create(user=user)
                return Response({"serializer": "serializer"})
            return Response(
                {"message": "error", "details": ["Invalid credentials"]})


login_api_view = LoginAPIView.as_view()


class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response({"message": "logouted"})

logout_api_view = LogoutAPIView.as_view()