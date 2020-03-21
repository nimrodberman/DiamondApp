from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadForm(FlaskForm):
    photo = FileField('Upload a picture of the diamond certificate', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
