from django.urls import path, include
# from . import views
from . views import register_user, JobApplicationViewSet, InteractionNoteViewSet 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('jobs', JobApplicationViewSet, basename="jobs")
router.register('notes', InteractionNoteViewSet, basename='notes')

urlpatterns = [
    path('register-user', register_user, name="register-user" ),
    path('', include(router.urls)),
    # NEW: The Login Endpoint (Get your Token here)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # NEW: Refresh Token Endpoint (Optional, but good practice)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
