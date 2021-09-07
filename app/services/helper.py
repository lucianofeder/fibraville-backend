import ipdb
from app.configs.database import db
from flask import jsonify
from http import HTTPStatus
from math import ceil
from app.exc import PageNotFound
from flask import request
from sqlalchemy import desc
from flask_mail import Message
from flask_restful import current_app
import ipdb


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
            data_list = [data.serializer() for data in data_list]
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


class EmailServices:
    
    @staticmethod
    def send_password(password, usuario):
        msg = Message('Senha para acesso plataforma Fibraville', recipients=[usuario.email])
        msg.html = f"<h1>Ola {usuario.nome}</h1><br><h2>Sua conta na Fibraville foi criada com sucesso</h2><br><br><p>Para acessar sua conta basta visitar nosso <a href=''>site</a> e ir na seccao acesso restrito. Use as seguintes credenciais:<br><ul><li>login: seu cpf</li><li>senha: {password}</li></ul>"
        current_app.mail.send(msg)
