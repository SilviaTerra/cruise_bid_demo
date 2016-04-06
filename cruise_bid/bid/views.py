from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Cruise
from .forms import bidForm, cruiseForm



def index(request):
	allCruises = Cruise.objects.all()
	context = {'allCruises': allCruises}
	return render(request, 'bid/index.html', context)

def placeBid(request, cruise_id):
    cruise = get_object_or_404(Cruise, pk=cruise_id)
    
    
    if request.method == 'POST':
        form = bidForm(request.POST)
        if form.is_valid(): 
            postBid = form.cleaned_data['newBid']
            if postBid > cruise.bid:
                cruise.bid = postBid
                cruise.save()
                #message = 'Success!'
                allCruises = Cruise.objects.all()
                context = {'allCruises': allCruises}
                return render(request, 'bid/index.html', context)
            else:
                form.is_valid = False
                message = 'Try again, your bid must exceed $%s/plot' % cruise.bid
                return HttpResponse(message)
    else:
        form = bidForm()
        
    	
    return render(request, 'bid/placeBid.html', {'cruise': cruise, 'form':form})
    
def submitCruise(request):
    if request.method == 'POST':
        newCruise = cruiseForm(request.POST)
        if newCruise.is_valid():
            Cruise.objects.create(name = newCruise.cleaned_data['name'],
                                state = newCruise.cleaned_data['state'],
                                numPlots = newCruise.cleaned_data['numPlots'],
                                bid = 0)
            allCruises = Cruise.objects.all()
            context = {'allCruises': allCruises}
            return render(request, 'bid/index.html', context)
    else:
        newCruise = cruiseForm()
    return render(request, 'bid/submitCruise.html', {'newCruise':newCruise})
    
    

