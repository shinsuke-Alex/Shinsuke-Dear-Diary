from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kawargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'what\'s on your mind?'})