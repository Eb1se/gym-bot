from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, ForeignKey, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

# Это для связи с базой (создадим позже)
from app.bot.database.base import Base

def utc_now():
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    telegram_id = Column(BigInteger(), unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=utc_now)
    last_activity = Column(DateTime, default=utc_now)
    is_active = Column(Boolean, default=True)

    settings = Column(JSON, default={
        "features": {
            "workout": True,      # тренировки
            "nutrition": True,    # КБЖУ
            "measurements": True, # замеры
            "cardio": True,       # кардио
            "weight": True,       # взвешивание
            "goals": True,        # цели
            "photos": True,       # фото прогресса
            "streak": True,       # Стрик
            "sleep": True,        # Сон
            "training_plan": True # План тренировок
        },

        "notifications": {
            "daily_reminder": False, 
            "workout_reminder": False
        }
        })
    
    workouts = relationship("Workout", back_populates="user")
    nutritions = relationship("Nutrition", back_populates="user")
    cardio = relationship("Cardio", back_populates="user")
    measurements = relationship("Measurements", back_populates="user")
    weight = relationship("Weight", back_populates="user")
    sleep = relationship("Sleep", back_populates="user")
    plans = relationship("Plan", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    progress_photos = relationship("ProgressPhoto", back_populates="user")

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(DateTime, default=utc_now)
    notes = Column(Text, nullable=True)
    training_time = Column(Float, nullable=False)
    quality = Column(Integer, nullable=True)

    user = relationship("User", back_populates="workouts")
    sets = relationship("Set", back_populates="workout")

class Set(Base):
    __tablename__ = "sets"
    id = Column(Integer, primary_key=True)

    workout_id = Column(Integer, ForeignKey("workouts.id"))
    exercise = Column(String, nullable=False)
    set_number = Column(Integer, nullable=False)
    weight = Column(Float, nullable= False)
    reps = Column(Integer, nullable=False)
    rest_time = Column(Integer, nullable=False)
    
    workout = relationship("Workout", back_populates="sets")

class Nutrition(Base):
    __tablename__ = "nutritions"
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    calories = Column(Integer, nullable=False)
    proteins = Column(Integer, nullable=False)
    fat = Column(Integer, nullable=False)
    carbs = Column(Integer, nullable=False)
    date = Column(DateTime, default=utc_now)

    user = relationship("User", back_populates="nutritions")


class Cardio(Base):
    __tablename__ = "cardio"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    time = Column(Float, nullable=False)
    pulse = Column(String, nullable=True)
    lost_calories = Column(Integer, nullable=True)
    datetime = Column(DateTime, default=utc_now)

    user = relationship("User", back_populates="cardio")


class Measurements(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    chest = Column(Float, nullable=True) #Грудь
    waistline = Column(Float, nullable=True) #Талия
    stomach = Column(Float, nullable=True) #Живот
    hips = Column(Float, nullable=True) #Бедра
    biceps = Column(Float, nullable=True) #Бицепс
    shoulders = Column(Float, nullable=True) #Плечи
    height = Column(Integer, nullable=True) #Рост

    user = relationship("User", back_populates="measurements")


class Weight(Base):
    __tablename__ = "weights"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float, nullable=False)
    date = Column(DateTime, default=utc_now)

    user = relationship("User", back_populates="weight") 

class Sleep(Base):
    __tablename__ = "sleep"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    time_sleep = Column(Float, nullable=False)
    quality = Column(Integer, nullable=False)

    user = relationship("User", back_populates="sleep")


class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    txt = Column(String, nullable=True)
    file_id = Column(String, nullable=True)
    file_unique_id = Column(String, unique=True)

    user = relationship("User", back_populates="plans")


class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    deadline = Column(DateTime, nullable=True)
    notes = Column(String, nullable=False)

    user = relationship("User", back_populates="goals")


class ProgressPhoto(Base):
    __tablename__ = "progress_photos"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    file_id = Column(String, nullable=False)
    file_unique_id = Column(String, unique=True)

    user = relationship("User", back_populates="progress_photos")
