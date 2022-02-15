from flask_app.config.mysqlconnection import connectToMySQL         
from flask import flash   

import re
from flask_app.models import info_model	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'
        result = connectToMySQL('nft_website').query_db(query,data)
        return result

    @classmethod
    def get_by_id(cls,**data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('nft_website').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('nft_website').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_one_users(cls,**data):
        query = 'SELECT * FROM users WHERE id = %(id)s;' 
        results = connectToMySQL('nft_website').query_db(query,data)
        if results:
            info = cls(results[0])
            return info


    @staticmethod
    def validate_registration(User):
        is_valid = True
        if len(User['first_name']) < 2:
            flash('First Name must be at least 3 characters.',"User")
            is_valid = False
        if len(User['last_name']) < 2:
            flash('Last Name must be at least 3 characters.',"User")
            is_valid = False
        if len(User['password']) < 8:
            flash('Password must be at least 8 characters.',"User")
            is_valid = False
        if User['password'] != User['confirm']:
            flash("Passwords don't match","User")
            is_valid = False
        if not EMAIL_REGEX.match(User['email']):
            flash("Invalid Email!","User")
            is_valid=False
        return is_valid 
    
