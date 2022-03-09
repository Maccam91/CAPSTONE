from flask_mongoengine.wtf import model_form
from flask_mongoengine import MongoEngine


db = MongoEngine()
class User(db.Document):
    email = db.StringField(required=True)
    username = db.StringField(max_length=12)
    password = db.StringField(min_length=8)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Post(db.Document):
    # title = db.StringField(max_length=120, required=True, validators=[validators.InputRequired(message='Missing title.'),])
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)

PostForm = model_form(Post)

def add_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST' and form.validate():
        # do something
        redirect('done')
    return render_template('add_post.html', form=form)