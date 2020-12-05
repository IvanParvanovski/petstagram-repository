from django.contrib.auth.forms import UserCreationForm


class BootstrapFormMixin():
    def setup_form(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
