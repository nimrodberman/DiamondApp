from wtforms import  SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class SearchForm(FlaskForm):
    shape = SelectField('Shape', [DataRequired()],
                       choices=[('BR', 'BR'),
                               ('CU', 'CU'),
                              ('OV', 'OV'),
                             ('PR', 'PR'),
                            ('PS', 'PS'),
                           ('RAD', 'RAD')])
    size = SelectField('Size', [DataRequired()],
                       choices=[('3','3'),
                               ('2.7-2.99', '2.7-2.99'),
                              ('2.4-2.69', '2.4-2.69'),
                             ('2.25-2.39', '2.25-2.39'),
                            ('2 - 2.24', '2 - 2.24'),
                           ('1.7 - 1.99', '1.7 - 1.99'),
                          ('1.5 - 1.69', '1.5 - 1.69'),
                         ('1.3 - 1.49', '1.3 - 1.49'),
                        ('1.2 - 1.29','1.2 - 1.29')])

    color = SelectField('Color', [DataRequired()],
                       choices=[('DE', 'DE'),
                               ('FG', 'FG'),
                              ('HJ', 'HJ'),
                             ('KM', 'KM'),])

    clarity = SelectField('Clarity', [DataRequired()],
                       choices=[('VS1', 'VS1'),
                               ('VS2', 'VS2'),
                              ('SI1', 'SI1'),
                             ('SI2', 'SI2'),])

    cut = SelectField('Cut', [DataRequired()],
                       choices=[('0', '0'),
                               ('1', '1'),
                              ('2', '2')])

    florecent = SelectField('Florecent', [DataRequired()],
                       choices=[('1', 'FAINT'),
                              ('0', 'NONE')])

    submit = SubmitField('Search')

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed('Image Only!'), FileRequired('Choose a file!')])
    submit = SubmitField('Upload')