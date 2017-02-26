# create a ModelForm class for each model that you wish to represent as a form.
# create or update a view to handle the form
    # including displaying the form
    # saving the form data, and
    # flagging up errors which may occure when the user enters incorrect data
    # in the form
# create or update a template to display the form
# add a urlpattern to map to the new view

from django import forms
from movies.models import Movie
import datetime

# Need to add a form to get movie info in the future
#class MovieForm(forms.ModelForm):
#    name = forms.CharField(max_length=128,help_text="Please enter Movie name.")
#    pubdate = forms.DateTimeField(widget=forms.HiddenInput(), default=datetime.date.today)
#    posterpath = forms.CharField(max_length=128,help_text="e.g images/m.jpg.")
#    basicinfo = forms.CharField(max_length=256,help_text="directer,writer,stars.")
#    synopsis = forms.CharField(max_length=512,help_text="synopsis.")
#    relatedlinks = forms.CharField(max_length=256,help_text="related links.")
#
#    class Meta:
#        model = Movie
#        fields('name', 'pubdate', 'posterpath', 'basicinfo', 'synopsis',
#                'relatedlinks')


# don't inherit from forms.ModelForm
class NavSearchForm(forms.Form):
    keywords = forms.CharField(max_length=128,help_text="please enter the movie name.")

