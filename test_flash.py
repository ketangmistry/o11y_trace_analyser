import pytest

import main


@pytest.fixture
def app():
    app = main.create_app()
    app.debug = True
    return app.test_client()


def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"The o11y Trace Analyser webapp" in res.data
