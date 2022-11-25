from rest_framework import routers

from ads.views.comment import CommentViewSet

router = routers.SimpleRouter()
router.register('comment', CommentViewSet)


urlpatterns = [

]

urlpatterns += router.urls
