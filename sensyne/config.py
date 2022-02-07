class BaseConfig:
    SECRET_KEY = "CmhK6vk2WW8yn784"
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db-sensyne/sensyne'


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    TESTING = True
