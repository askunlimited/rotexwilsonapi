from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

User = get_user_model()


class RegisterView(APIView):
    permission_classes = permissions.AllowAny

    def post(self, request):
        try:
            data = request.data

            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            email = email.lower()
            phone = phone["phone"]
            password = data["password"]
            re_password = data["re_password"]
            is_vendor = data["is_vendor"]

            if is_vendor == "True":
                is_vendor = True
            else:
                is_vendor = False

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_vendor:
                            User.objects.create_user(
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone=phone,
                                password=password,
                            )
                            return Response(
                                {
                                    "success": "User created successfully, check your email to verify your account"
                                },
                                status=status.HTTP_201_CREATED,
                            )
                        else:
                            User.objects.create_vendor(
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone=phone,
                                password=password,
                            )
                            return Response(
                                {
                                    "success": "Vendor account created successfully, check your email to verify your account"
                                },
                                status=status.HTTP_201_CREATED,
                            )
                    else:
                        return Response(
                            {"error": "User with this email already exists"}
                        )
                else:
                    return Response(
                        {"error": "Password must not be less than 8 characters"}
                    )

            else:
                return Response(
                    {"error": "Passwords do not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except:
            return Response(
                {"error": "Something went wrong when registering account"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
