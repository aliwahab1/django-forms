from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet

# class NumeWidget(forms.MultiWidget):

#     def __init__(self, attrs=None):
#         super().__init__([
#             forms.TextInput(),
#             forms.TextInput()
#         ], attrs)

#     def decompress(self, value):
#         #'firstvalue secondvalue'
#         if value:
#             return value.split(' ')
#         return ['', '']
#         # data_list = ['firstvalue', 'secondvalue']
    



class NameField(forms.MultiValueField):

    # widget = NameWidget

    def __init__(self, *args, **kwargs):

        fields = (
            forms.CharField(), # test
            forms.CharField(), # none
        )

    def compress(self, data_list):
        # data_list = ['test', 'none']
        # data_list = ['firstvalue', 'secondvalue']
        return f'{data_list[0]} {data_list[1]}'
        #'firstvalue secondvalue'




class ContactForm(forms.Form):
    name = forms.CharField()
    # name = NameField(),
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'question'), ('other', 'other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"

        self.helper.layout =Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'body')