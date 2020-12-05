from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.clean_up import clean_up_files
from pets.forms.comment import CommentForm
from pets.forms.pets import PetCreateForm
from pets.models.comment import Comment
from pets.models.like import Like
from pets.models.pet import Pet


@login_required
def list_pets(req):
    context = {
        'pets': Pet.objects.all()
    }

    return render(req, 'pet_list.html', context=context)


@login_required
def show_pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == 'GET':
        form = CommentForm()

        context = {
            'pet': pet,
            'comment_form': form,
            'can_edit': req.user == pet.user.user,
            'can_delete': req.user == pet.user.user,
            'can_like': req.user != pet.user.user,
            'can_comment': req.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=req.user.userprofile.id).exists(),
        }

        return render(req, 'pet_detail.html', context=context)
    else:
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = Comment(
                comment=form.cleaned_data['comment'],
                user=req.user.userprofile,
            )
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)

        context = {
            'pet': pet,
            'comment_form': form,
        }

        return render(req, 'pet_detail.html', context=context)


    # if req.method == 'GET':
    #     comment_form = CommentForm()
    # else:
    #     comment_form = CommentForm(req.POST)
    #     if comment_form.is_valid():
    #         comment_form.save()
    #         return redirect('pet details', pk)


@login_required
def like_pet(req, pk):
    like = Like.objects.filter(user_id=req.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(user=req.user.userprofile)

        like.pet = pet
        like.save()

    return redirect('list pets')


@login_required
def create_pet(req):
    if req.method == 'GET':
        context = {
            'create_form': PetCreateForm(),
        }

        return render(req, 'pet_create.html', context=context)
    else:
        form = PetCreateForm(req.POST,
                             req.FILES)

        if form.is_valid():
            form.save()
            return redirect('list pets')

        context = {
            'create_form': form,
        }

        return render(req, 'pet_create.html', context=context)


@login_required
def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == 'GET':
        form = PetCreateForm(instance=pet)
        context = {
            'form': form,
        }

        return render(req, 'pet_edit.html', context=context)

    else:
        old_image = pet.image
        form = PetCreateForm(req.POST,
                             req.FILES,
                             instance=pet)
        if form.is_valid():
            clean_up_files(old_image.path)
            form.save()
            return redirect('pet details or comment', pk)

        context = {
            'form': form,
        }

        return render(req, 'pet_edit.html', context=context)


@login_required
def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(req, 'pet_delete.html', context=context)
    else:
        pet.delete()
        return redirect('list pets')
