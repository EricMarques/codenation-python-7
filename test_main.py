from main import get_temperature
import requests
import pytest


# valores a serem utilizados

lat = -14.235004
lng = -51.92528
temperature = 62
expected = 16


class MockResponse:
    @staticmethod
    def json():
        return { "currently": { "temperature": temperature } }

    def test_get_json(monkeypatch):
        def mockget(*args, **kwargs):
            return MockResponse()

        monkeypatch.__setattr__(requests, "get", mock_get)


@pytest.mark.parametrize("lat, lng, expect", [(lat,
                                               lng,
                                               expected)])
def test_get_temperature_by_lat_lng(lat, lng, expect, monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = get_temperature(lat, lng)

    assert result == expect