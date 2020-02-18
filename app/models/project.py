from sqlalchemy import DateTime

from ..core import db
from ..core import ma


class Project(db.Model):
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    urls = db.Column(db.Text)
    techstack = db.Column(db.Text)
    is_active_status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
   
    def __init__(self,name):
        self.name = name
        self.is_active_status = is_active_status


class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('name', 'is_active_status')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

