from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Name must start with A or a')
### note that only value is used as parameter it is keyword

class formclass(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    recheckemail=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    ###cleaning of full data
    def clean(self):
        formdata=super().clean()
        if formdata['email']!=formdata['recheckemail']:
            raise forms.ValidationError('Email must be same')
    #####
    ###manually created validator
    # def clean_botcatcher(self):
    #     bot_catcher=self.cleaned_data['botcatcher']
    #     if len(bot_catcher)>0:
    #         raise forms.ValidationError("Hey you i got you")
    #####################
