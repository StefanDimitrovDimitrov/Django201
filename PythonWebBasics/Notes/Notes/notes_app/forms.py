from django import forms

from Notes.notes_app.models import Profile, Note


class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ('profile',)


class DeleteNoteForm(NoteForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
