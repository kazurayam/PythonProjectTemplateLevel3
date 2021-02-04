import sys
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

# update sys.path to include the 'src' directory in the Module-Search path
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/"))


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    '''
    The app fixture will call the factory and
    pass test_config to configure the application and
    database for testing instead of using your local
    development configuration
    '''
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    '''For most of the views, a user needs to be logged in.
    The easiest way to do this in tests is to make a POST request
    to the login view with the client. Rather than writing
    that out every time, you can write a class with methods
    to do that, and use a fisture to pass it the client
    for each test.
    '''
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
