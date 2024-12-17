from django.urls import path, include
from Post.views import Postviewset, Commentviewset, Tagviewset, Categoryviewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"posts", Postviewset)
router.register(r"comments", Commentviewset)
router.register(r"tags", Tagviewset)
router.register(r"categories", Categoryviewset)

urlpatterns = [
    path('', include(router.urls)),
]
