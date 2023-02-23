from django.db.models import EmailField
from django.forms import ModelForm, TextInput
from .models import User


class AddForm(ModelForm):
    class Meta:
        model = User
        fields = {'email'}

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Введите ваш E-mail',
                'class': 'input-calss_name'
            })
