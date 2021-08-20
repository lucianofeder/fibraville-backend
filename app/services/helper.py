from app.configs.database import db

class BaseServices():
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

def add_commit(data):
    db.session.add(data)
    db.session.commit()