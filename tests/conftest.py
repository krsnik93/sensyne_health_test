import os
import tempfile

import pytest

from sensyne.app import create_app
from sensyne.utils import init_db
from sensyne.config import TestConfig

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client