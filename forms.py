from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired


class CreateForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
