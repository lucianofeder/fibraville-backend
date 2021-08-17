from flask_restful import current_app

class BaseServices():
    def save(self):
        current_app.session.add(self)
        current_app.session.commit()
