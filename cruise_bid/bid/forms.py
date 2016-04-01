from django import forms

class bidForm(forms.Form):
	newBid = forms.DecimalField(max_digits=5, decimal_places=2)
	
class cruiseForm(forms.Form):
	name = forms.CharField(max_length=200)
	state = forms.CharField(max_length=200)
	numPlots = forms.IntegerField()
	