from django.urls import path
from .views import NewMemberViews


urlpatterns = [
    path('new-member/', NewMemberViews.as_view()),
    path('new-member/<int:id>', NewMemberViews.as_view())
]
