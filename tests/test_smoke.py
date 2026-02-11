from unittest.mock import patch

import pytest
from django.template.loader import get_template


def test_templates_namespace_loads():
    get_template("django_starter_core/components/page_header.html")
    get_template("django_starter_core/about/index.html")


def test_jwt_generate_and_decode():
    from django_starter_core.contrib.auth.services import decode, generate_token

    token = generate_token({"user_id": 1, "username": "u"})
    payload = decode(token.token)
    assert payload
    assert payload["user_id"] == 1
    assert payload["username"] == "u"


@pytest.mark.django_db
def test_monitoring_ninja_health_sync_endpoint(client):
    with patch("django_starter_core.contrib.monitoring.apis.check_db_sync", return_value=True), patch(
        "django_starter_core.contrib.monitoring.apis.check_redis_sync", return_value=True
    ):
        resp = client.get("/api/django-starter/monitoring/health/sync")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["status"] in {"healthy", "unhealthy"}
