from django.urls import path, include
# from . import views
from . views import register_user, JobApplicationViewSet, InteractionNoteViewSet 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('jobs', JobApplicationViewSet, basename="jobs")
router.register('notes', InteractionNoteViewSet, basename='notes')

urlpatterns = [
    path('auth/register', register_user, name="register-user" ),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('', include(router.urls)),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
