from django.urls import path
from .views import recipeDraftPageView, currentDraftsPageView, draftPublishedPageView

urlpatterns = [
path("recipedraft/", recipeDraftPageView, name="recipedraft"),
path("currentdrafts/", currentDraftsPageView, name="currentdraft"),   
path("draftpublished/", draftPublishedPageView, name="draftpublished"), 
]         