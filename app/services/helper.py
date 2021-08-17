from flask_restful import current_app

class BaseServices():
    def save(self):
        current_app.session.add(self)
        current_app.session.commit()

def add_commit(data):
    current_app.session.add(data)
    current_app.session.commit()