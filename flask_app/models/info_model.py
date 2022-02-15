from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash              

from flask_app.models import user_model  




class Info:
    def __init__(self, data):
        self.id = data['id']
        self.about = data['about']
        self.location = data['location']
        self.relationship_status = data['relationship_status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save_info(cls,data):
        query = 'INSERT INTO info (about,location,relationship_status, user_id) VALUES (%(about)s,%(location)s,%(relationship_status)s, %(user_id)s);'
        result = connectToMySQL('nft_website').query_db(query,data)
        return result
    
    @classmethod
    def get_one_profile(cls,**data):
        query = 'SELECT * FROM info WHERE id = %(id)s;' 
        results = connectToMySQL('nft_website').query_db(query,data)
        if results:
            info = cls(results[0])
            return info

    @classmethod
    def get_one(cls,**data):
        query = 'SELECT * FROM info WHERE user_id = %(user_id)s;' 
        result = connectToMySQL('nft_website').query_db(query,data)
        if result:
            return cls(result[0])

    @classmethod
    def update(cls,data):
        query = 'UPDATE info SET about=%(about)s,location=%(location)s,relationship_status=%(relationship_status)s, updated_at=NOW() WHERE user_id = %(user_id)s;'
        return connectToMySQL('nft_website').query_db(query,data)