import pytest

from app import app

# This fixture is used to test the app context
@pytest.fixture(scope='module')
def test_app():
    with app.app_context():
        yield app.test_client()