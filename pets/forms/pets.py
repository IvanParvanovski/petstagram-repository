from django import forms

from pets.models.pet import Pet


class PetCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        exclude = ('user', )
        # widgets = {
        #     'type': forms.Select(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        #
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        #
        #     'age': forms.NumberInput(
        #         attrs={
        #             'class': 'form-control'
        #         },
        #     ),
        #
        #     'image_url': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         },
        #     ),
        #
        #     'description': forms.Textarea(
        #         attrs={
        #             'class': 'form-control'
        #         },
        #     ),
        # }
