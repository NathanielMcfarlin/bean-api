"""
URL configuration for bean project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from beanapi.views import (
    UserViewSet,
    DrinkViewSet,
    PreferenceViewSet,
    OrderedDrinkViewSet,
    OrdersViewSet,
    CartViewSet,
    PastOrderedDrinkViewSet
)

router = DefaultRouter(trailing_slash=False)
router.register(r"drinks", DrinkViewSet, "drink")
router.register(r"preferences", PreferenceViewSet, "preference")
router.register(r"orders", OrdersViewSet, "order")
router.register(r"ordered_drinks", OrderedDrinkViewSet, "ordered_drinks")
router.register(r"cart", CartViewSet, "cart")
router.register(r"past_orders", PastOrderedDrinkViewSet, "past_orders")

urlpatterns = [
    path("", include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path(
        "register", UserViewSet.as_view({"post": "register_account"}), name="register"
    )
]