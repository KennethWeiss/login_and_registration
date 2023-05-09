from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "login_registration"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """INSERT INTO user (first_name, last_name, email, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results