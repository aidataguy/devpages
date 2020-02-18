from sqlalchemy import DateTime

from ..core import db
from ..core import ma



class Author(db.Model):
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    social = db.Column(db.Text)
    password = db.Column(db.String(15))
    email = db.column(db.Text)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
   
    def __init__(self, username, email, social, password):
        self.username = username
        self.email = email
        self.social = social
        self.password = password



class AuthorSchema(ma.Schema):
    class Meta:
        hidden_fields=('passwords')
        fields = ('username', 'email', 'social')


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)



