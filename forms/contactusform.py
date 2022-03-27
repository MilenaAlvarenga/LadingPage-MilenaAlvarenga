from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class contactme(FlaskForm):
    fullname = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Nombre completo"},
    )
    
    email = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Email"},
    )
    
    message = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=300),
        ],
        render_kw={"placeholder": "Mensaje"},
    )

    submit = SubmitField("submit")
