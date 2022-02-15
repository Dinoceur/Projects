from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

from flask_app.models import user_model


class Post:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.link = data['link']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_post(cls,data):
        query = 'INSERT INTO posts (link,content) VALUES (%(link)s,%(content)s);'
        result = connectToMySQL('nft_website').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL('nft_website').query_db(query)
        posts = []
        for u in results:
            posts.append( cls(u) )
        return posts

    @classmethod
    def get_one_post(cls,**data):
        query = 'SELECT * FROM posts JOIN users ON users.id = posts.user_id WHERE posts.id = %(id)s;' 
        results = connectToMySQL('nft_website').query_db(query,data)
        if results:
            row = results[0]
            post = cls(row)
            user_data = {
                **row,
                "id": row ["users.id"],
                "link": row ["link.id"],
                "content": row ["content.id"],
                "created_at": row ["users.created_at"],
                "updated_at": row ["users.updated_at"]
            }
            post.user= user_model.User(user_data)
            return post