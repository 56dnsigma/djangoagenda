from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para o usuário',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro2',
                code='invalid'
            )
        )

        return super().clean()