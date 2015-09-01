from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.layout import Div, Field, Fieldset, HTML, Layout, Submit
from django import forms

from .models import Answer

class IndexForm(forms.ModelForm):

    YES_NO = ((True, 'Yes'), (False, 'No'))

    present = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO)

    class Meta:
        model = Answer
        fields = ('present',)

    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Next >>'))

