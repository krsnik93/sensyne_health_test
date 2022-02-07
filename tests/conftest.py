import os
import tempfile

import pytest

from sensyne.app import create_app
from sensyne.utils import init_db


@pytest.fixture
def client():
    app = create_app(**{
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/test.db'
    })
    with app.test_client() as client:
        yield client