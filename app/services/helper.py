from app.configs.database import db
from flask import jsonify
from http import HTTPStatus
from math import ceil
from app.exc import PageNotFound

class BaseModel():
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def __lt__(self, other):
    #     if isinstance(other, BaseModel):
    #         return self.id < other.id

    # def __gt__(self, other):
    #     if isinstance(other, BaseModel):
    #         return self.id > other.id


class BaseServices():
    model = None


    @classmethod
    def get_all(cls):
        data_list = cls.model.query.order_by(cls.model.id).all()
        return jsonify(BaseServices.paginate(data_list)), HTTPStatus.OK
    

    @classmethod
    def get_by_id(cls, id):
        data = cls.model.query.get(id)
        if data:
            return jsonify(data), HTTPStatus.CREATED
        return {}, HTTPStatus.NOT_FOUND

    
    @classmethod
    def delete(cls, id):
        data = cls.model.query.get(id)
        if data:
            data.delete()
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def paginate(data_list, per_page=15, page=1):
        last_page = ceil(len(data_list)/per_page)
        if page < 1 or page > last_page:
            raise PageNotFound(page)

        # if len(data_list) > 0 and 'id' in data_list[0]:
        #     data_list = sorted(data_list, key=lambda k: k['id']) 

        previous_page = None
        next_page = None

        if len(data_list) < last_page:
            next_page = page + 1
        
        if page > 1:
            previous_page = page - 1
        
        return {
            "page": page,
            "previous_page": previous_page,
            "next_page": next_page,
            "data": data_list[((page-1)*per_page):(page*per_page)]
        }
