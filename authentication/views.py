from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerializer,UserListSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#user list dekhar jonno
class UserListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserListSerializer(user, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user view detail kore dekhar jonno
class UserDetailAPIView(APIView):    
     def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        serializer = UserListSerializer(user)
        return Response(serializer.data)
     
     def put(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        serializer = UserListSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
     
     def delete(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#user account created
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)
            confirm_link = f'http://127.0.0.1:8000/authentication/active/{uid}/{token}/'
            email_subject = 'Confirm Your Email'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response({'detail' : 'Check Your Email For Confirmation'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user activat hobe link diye
def user_activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(request)

    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')       

#user je account create koreche ejonno se ekon web site e probesh korbe
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']    
            password = serializer.validated_data['password']    
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
#user website theke bahir hobe        
class LogoutAPIView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()

        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

#user tar password ta jeno reset dite pare
class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return Response({"error": "No User With This Email"}, status=status.HTTP_400_BAD_REQUEST)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))   
        reset_link = f'http://127.0.0.1:8000/password_reset/{uid}/{token}/'
        email_subject = 'Password Reset Request'
        email_body = render_to_string('reset_password_email.html', {'reset_link': reset_link})
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()

        return Response({"detail": "Password Reset Email Sent"}, status=status.HTTP_200_OK)

    
#user tar password ta jeno reset er jonno confirm korte parbe
class PasswordResetConfirmView(APIView):
    def post(self, request, token, uidb64):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')

            if password != confirm_password:
                return Response({"error": "Passwords Do Not Match"}, status=status.HTTP_400_BAD_REQUEST)

            if len(password) < 8:
                return Response({"error": "Password must be at least 8 characters long"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(password)
            user.save()
            return Response({"detail": "Password Has Been Reset Successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid Token Or User"}, status=status.HTTP_400_BAD_REQUEST)