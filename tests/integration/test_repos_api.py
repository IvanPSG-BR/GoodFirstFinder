import pytest


@pytest.mark.asyncio
async def test_list_repositories_empty(client):
    response = await client.get("/api/v1/repos/")
    assert response.status_code == 200
    data = response.json()
    assert data["items"] == []
    assert data["total"] == 0


@pytest.mark.asyncio
async def test_get_repository_not_found(client):
    import uuid

    fake_id = str(uuid.uuid4())
    response = await client.get(f"/api/v1/repos/{fake_id}")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
