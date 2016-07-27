# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .models import Note

from django.shortcuts import render

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


# Below is the view function for the Notes model

def notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {"notes": notes})


#def search(request):
#    if request.method == 'POST':
#        query = request.POST['query']
#        results = Note.objects.filter(user=request.user, note__contains=query)
#        return  render(request, 'search.html', {'results':results})
#    return HttpResponse('Nothing to see here, Move along.')

# Below is the view function for the Note model for a new saved note
def note(request):
    if request.method == 'POST':
        note = Note.objects.filter(user=request.user)
        return render(request, 'note.html', {"note": note})
    return HttpResponse('Nothing to see here, Move along.')


#def get_note(note_id): # request from browser
    """When you click on a note in notes-list it will load it into the active window on the right"""








#def get_notes_list(user_id): # request from browser
    """When you log in to the database get and return to the browser the notes from the database"""








#def get_page_by_username(): # response by server
    """Get everything on the page and return it to the browser"""









#def get_note_response(): # response by server
    """As a logged in user when you click on a note send and load that note into the active window on the right"""

