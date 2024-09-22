from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.models import EmailAddress
from rest_framework import status
# Create your views here.

# class CustomConfirmEmailView(APIView):
#     def get(self, request, key):
#         try:
#             email_address = EmailAddress.objects.get(key=key)
#             email_address.verified = True
#             email_address.save()
#             return Response({"detail": "Email confirmed successfully."}, status=status.HTTP_200_OK)
#         except EmailAddress.DoesNotExist:
#             return Response({"detail": "Invalid confirmation key."}, status=status.HTTP_400_BAD_REQUEST)
        
# class RegistrationView(generics.CreateAPIView):
#     serializer_class = RegistrationSerializer
#     permission_classes = [AllowAny]