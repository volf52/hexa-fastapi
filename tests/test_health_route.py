# -*- coding: utf-8 -*-


async def test_health(test_client):
    response = await test_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
