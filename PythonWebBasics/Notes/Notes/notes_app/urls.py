
'''
•	http://localhost:8000/ - home page
•	http://localhost:8000/add - add note page
•	http://localhost:8000/edit/:id - edit note page
•	http://localhost:8000/delete/:id - delete note page
•	http://localhost:8000/details/:id - note details page
•	http://localhost:8000/profile - profile page



'''
from django.urls import path

from Notes.notes_app.views import home, add_note, edit_note, delete_note, details_note, profile_page, delete_profile, \
    create_profile

urlpatterns = [

    path('', home, name='home_page'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>', edit_note, name='edit_note'),
    path('delete/<int:pk>', delete_note, name='delete_note'),
    path('details/<int:pk>', details_note, name='details_note'),
    path('profile/', profile_page, name='profile_page'),
    path('crate_profile/', create_profile, name='create profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),




]