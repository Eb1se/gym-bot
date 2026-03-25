from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

TestBase = declarative_base()

class User(TestBase):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)

def test_user_creation():
    user = User(
        telegram_id=123456789,
        username="Eb1se",
        first_name="Максим"
    )
    assert user.telegram_id == 123456789
    assert user.username == "Eb1se"
    assert user.first_name == "Максим"

#запуск python -m pytest tests/test_database/test_models.py -v