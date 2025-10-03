from django.shortcuts import render
from .models import Movie
from .models import Petition
from .forms import PetitionForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

# Create your views here.

def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})


def petitions_list(request):
    petitions = Petition.objects.order_by('-created_at')
    template_data = {'title': 'Petitions', 'petitions': petitions}
    return render(request, 'movies/petitions.html', {'template_data': template_data})


@login_required
def petition_create(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            # optionally add the creator as a voter
            petition.voters.add(request.user)
            return redirect('movies.petitions')
    else:
        form = PetitionForm()
    template_data = {'title': 'Create Petition', 'form': form}
    return render(request, 'movies/petition_create.html', {'template_data': template_data})


@login_required
def petition_vote(request, id):
    petition = get_object_or_404(Petition, id=id)
    if request.user in petition.voters.all():
        petition.voters.remove(request.user)
    else:
        petition.voters.add(request.user)
    return redirect('movies.petitions')
