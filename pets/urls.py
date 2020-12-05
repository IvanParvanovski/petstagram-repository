from django.urls import path
from pets.views import \
    list_pets,\
    show_pet_detail,\
    like_pet,\
    create_pet,\
    edit_pet,\
    delete_pet

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('details/<int:pk>', show_pet_detail, name='pet details or comment'),
    path('like/<int:pk>', like_pet, name='like pet')
]
