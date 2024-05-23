from httpx import AsyncClient
from main import app, BAD_REQUEST_ANSWER
import pytest
from freezegun import freeze_time


DEFAULT_JSON = {
                  "Columns": [
                    "key1",
                    "key2",
                    "key3"
                  ],
                  "Description": "string",
                  "RowCount": 1,
                  "Rows": [
                    [
                      132,
                      "2024-05-23 07:22:55",
                      "test1"
                    ]
                  ]

                }

DEFAULT_TODAY_TIME = "2024-05-23 12:00:00"  # для заморозки данных


@freeze_time(DEFAULT_TODAY_TIME)
@pytest.mark.anyio
async def test_task6_handler_main_correct():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/very/important/docs?documents_date=2024-05-23%2000%3A00%3A00",
                                 json=DEFAULT_JSON)
    assert response.status_code == 200


@freeze_time(DEFAULT_TODAY_TIME)
@pytest.mark.anyio
async def test_task6_handler_main_uncorrect_input_datetime():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/very/important/docs?documents_date=2024-05-23%2012%3A10%3A05",
                                 json=DEFAULT_JSON)
    assert response.status_code == 400
    assert  response.json() == BAD_REQUEST_ANSWER




