from sqlalchemy import DateTime

from slugify import slugify

from ..core import db
from ..core import ma

from .author import Author

class Blog(db.Model):
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    hero_image = db.Column(db.Text)
    blog_image = db.Column(db.Text, default=False)
    slug = db.Column(db.String(20))
    author = db.Column(db.ForeignKey(Author.id))
    created_at = db.Column(db.DateTime)

    def __init__(self, title, *args, **kwargs ):
        self.title = title
        self.description = hero_image
        self.hero_image = hero_image 
        self.blog_image = blog_image
        self.slug = slug

        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('title', 'description', 'hero_image',
         'blog_image', 'slug')

blog_schema = BlogSchema()
blogs_schemas_schema = BlogSchema(many=True)


