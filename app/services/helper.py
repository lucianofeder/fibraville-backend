import ipdb
from app.configs.database import db
from flask import jsonify
from http import HTTPStatus
from math import ceil
from app.exc import PageNotFound
from flask import request
from sqlalchemy import desc


class BaseModel():
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class BaseServices():
    model = None


    @classmethod
    def get_all(cls):
        try:
            data_list = cls.model.query.order_by(desc(cls.model.id)).all()
            return jsonify(BaseServices.paginate(data_list)), HTTPStatus.OK
        except PageNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
        except ValueError as e:
            return {"error": str(e)}, HTTPStatus.BAD_REQUEST


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
        per_page = int(request.args.get('per_page', per_page))
        page = int(request.args.get('page', page))
        last_page = ceil(len(data_list)/per_page)

        if last_page == 0:
            return {
                "page": page,
                "previous_page": None,
                "next_page": None,
                "data": []
            }

        if page < 1 or page > last_page:
            raise PageNotFound(page)

        previous_page = None
        next_page = None

        if page < last_page:
            next_page = page + 1
        
        if page > 1:
            previous_page = page - 1
        
        return {
            "page": page,
            "previous_page": f'page={previous_page}&per_page={per_page}' if previous_page else previous_page,
            "next_page": f'page={next_page}&per_page={per_page}' if next_page else next_page,
            "data": data_list[((page-1)*per_page):(page*per_page)]
        }
