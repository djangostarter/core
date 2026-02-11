from ninja import NinjaAPI
from django.urls import include, path

from django_starter_core.apis import router as core_api_router

api = core_api_router.api
if api is None:
    api = NinjaAPI(title="django-starter-core-tests", version="1.0")
    api.add_router("/django-starter", core_api_router)

urlpatterns = [
    path("api/", api.urls),
    path("", include("django_starter_core.urls")),
]
