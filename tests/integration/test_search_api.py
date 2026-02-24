import pytest


@pytest.mark.asyncio
async def test_search_empty_results(client):
    response = await client.get("/api/v1/search/")
    assert response.status_code == 200
    data = response.json()
    assert data["items"] == []
    assert data["total"] == 0


@pytest.mark.asyncio
async def test_search_with_language_filter(client):
    response = await client.get("/api/v1/search/?language=Python")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["items"], list)


@pytest.mark.asyncio
async def test_search_pagination_defaults(client):
    response = await client.get("/api/v1/search/")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
    assert data["per_page"] == 20
