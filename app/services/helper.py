from app.configs.database import db

class BaseServices(db.Model):
    def save(self):
        db.session.add(self)
        db.session.commit()
