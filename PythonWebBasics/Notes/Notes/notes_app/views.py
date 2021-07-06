from django.shortcuts import render, redirect

# Create your views here.
from Notes.notes_app.forms import NoteForm, DeleteNoteForm, ProfileForm
from Notes.notes_app.models import Profile, Note


def home(request):

    main_profile = Profile.objects.first()

    notes = Note.objects.all()

    if not main_profile:
        return redirect('create profile')


    context = {
        'profile': main_profile,
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context)




def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)




def add_note(request):
    note = Note()
    if request.method == "POST":

        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.profile = Profile.objects.first()
            note.save()
            form.save()
            return redirect('home_page')

    context = {
        'form': NoteForm(),
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":

        form = NoteForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('home_page')

    context = {
        'form': NoteForm(instance=note),
        'expense': note
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect('home_page')
    context = {
        'note': note,
        'form': DeleteNoteForm(instance=note)
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.count()

    if request.method == 'GET':
        context = {
            'profile': profile,
            'notes': notes
        }
        return render(request, 'profile.html', context)

    profile.delete()
    return redirect('home_page')


def delete_profile(request):
    profile = Profile.objects.first()
    profile.delete()
    return redirect('home_page')
