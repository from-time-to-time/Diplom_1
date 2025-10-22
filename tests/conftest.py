import pytest
from praktikum.database import Database
@pytest.fixture
def db() -> Database:
    return Database()