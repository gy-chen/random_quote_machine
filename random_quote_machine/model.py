# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from random_quote_machine import setting

engine = create_engine(setting.DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)

    quotes = relationship('Quote', order_by='Quote.id', back_populates='video')


class Quote(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True)
    quote = Column(String)
    video_id = Column(Integer, ForeignKey('video.id'))

    video = relationship('Video', back_populates="quotes")


def model_to_dict(model):
    result = dict(model.__dict__)
    result.pop('_sa_instance_state')
    return result


Base.metadata.create_all(engine)
