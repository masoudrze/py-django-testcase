from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import JsonResponse

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        auth_login(request, user)

        return JsonResponse(
            {"message": "login ok"},
            status=200
        )

    return JsonResponse(
        {"message":"login not valid"},
        status=401
    )

    # if username == "admin" and password == "123456":
    #     return JsonResponse(
    #         {"message": "Login is ok"},
    #         status=200
    #     )
    # return JsonResponse(
    #     {"message":"invalid"},
    #     status=401
    # )
