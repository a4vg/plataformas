from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# For users
cacheusers = {}
# For messages
cachemessages = {}

#------------------------------ Database declaration ------------------------------------


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sendby = Column(String(50))
    receiveby = Column(String(50))
    message = Column(String(50))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(12))
    fullname = Column(String(50))


#--------------------------- Important stuff -----------------------------------------------
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#--------------------------- Fill database -----------------------------------------------
def setusers():
    global cacheusers
    if cacheusers == {}:  # if empty
        #engine = create_engine('sqlite:///:memory:', echo=True)
        #engine = create_engine('sqlite:////mydb', echo=True)
        # Base.metadata.create_all(engine)

        #Session = sessionmaker(bind=engine)
        #session = Session()

        userstocommit = []

        userstocommit.append(User(id=1, username='ironduck',
                                  password='capsucks', fullname='Tony Stark'))
        userstocommit.append(User(id=2, username='capiduckmerica',
                                  password='makeduckmericagreatagain', fullname='Steve Rogers'))
        userstocommit.append(
            User(id=3, username='dulk', password='dulkSMASH', fullname='Bruce Banner'))
        userstocommit.append(User(id=4, username='dhor', password='missmyhammer',
                                  fullname='Thor, King of Ducksgard'))
        userstocommit.append(User(id=5, username='duckwidow',
                                  password='rocketsmyex', fullname='Natasha Duckmanoff'))
        userstocommit.append(User(id=6, username='duckeye',
                                  password='strongestavenger', fullname='Clint Barton'))
        userstocommit.append(User(id=7, username='spiderduck',
                                  password='falta', fullname='Peter Ducker'))
        userstocommit.append(User(id=8, username='pepper',
                                  password='falta', fullname='Pepper Pots'))
        userstocommit.append(User(id=9, username='duckfury',
                                  password='falta', fullname='Duck Fury'))
        userstocommit.append(User(id=10, username='mantis',
                                  password='sleeep', fullname='Duck Mantis'))
        userstocommit.append(User(id=11, username='iamgroot',
                                  password='iamgroot', fullname='Groot the Duck'))
        userstocommit.append(User(id=12, username='superduckman',
                                  password='falta', fullname='Dlarck Kent'))

        for u in userstocommit:
            session.add(u)

        session.commit()

        listin = session.query(User)

        for i in listin:
            cacheusers[i.username] = [i.password, i.fullname]

    return


def setmessages():
    if cachemessages == {}:

        messagestocommit = []

        messagestocommit.append(Message(id=1, receiveby='ironduck',
                                        sendby='spiderduck', message='Mr. Stark, I don\'t wanna go'))
        messagestocommit.append(Message(id=2, receiveby='ironduck',
                                        sendby='duckwidow', message='I\'ve located Steve Rogers'))
        messagestocommit.append(Message(id=3, receiveby='ironduck',
                                        sendby='pepper', message='Miss you'))
        messagestocommit.append(Message(id=4, receiveby='ironduck',
                                        sendby='duckfury', message='Come back, NOW'))
        messagestocommit.append(Message(id=5, receiveby='ironduck',
                                        sendby='capiduckmerica', message='He killed my father!'))
        messagestocommit.append(Message(id=6, receiveby='ironduck',
                                        sendby='duckmantis', message='SLEEPPPP!!!!!'))
        messagestocommit.append(Message(id=7, receiveby='ironduck',
                                        sendby='iamgroot', message='I am Duck Groot'))
        messagestocommit.append(Message(id=8, receiveby='ironduck',
                                        sendby='dulk', message='Why wont it come out!'))
        messagestocommit.append(Message(id=9, receiveby='ironduck', sendby='ironduck',
                                        message='Out of 14 millions we one have ONE chance'))
        messagestocommit.append(Message(id=10, receiveby='ironduck', sendby='superduckman',
                                        message='My movies are horrible, can I join the Avengers?'))

        for m in messagestocommit:
            session.add(m)
        session.commit()

        # Meter mensajes en el cache
        listin = session.query(Message)
        for i in listin:
            cachemessages[i.id] = [i.sendby, i.receiveby, i.message]

    return
