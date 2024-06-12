import pytest
from application import create_app
from application.extensions import db

@pytest.fixture(scope='module')
def test_app():
    app = create_app(testing=True)
    return app

@pytest.fixture(scope='module')
def test_database(test_app):
    with test_app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()
