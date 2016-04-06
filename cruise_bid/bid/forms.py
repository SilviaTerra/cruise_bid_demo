from bid.models import Cruise
from django import forms
from django.forms import ModelForm

class bidForm(forms.Form):
	newBid = forms.DecimalField(max_digits=5, decimal_places=2)
	
	
class cruiseForm(ModelForm):
    class Meta:
        model = Cruise
        fields = ['name', 'state', 'numPlots']
