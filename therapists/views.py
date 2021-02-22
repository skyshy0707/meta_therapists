from django.shortcuts import render

# Create your views here.

from .models import Therapist


def therapists(request):
	therapists = Therapist.objects.all()
	print("num of therapists: ", len(therapists))
	return render(request, 'therapists.html', {'therapists': therapists})

def therapist(request, pk):
	try:
		therapist = Therapist.objects.get(pk=pk)
	except Therapist.DoesNotExist:
		return render(request, 'therapist_404.html', {})

	return render(request, 'therapist.html', {'therapist': therapist})