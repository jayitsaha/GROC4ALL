from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from products.models import Product
from users.models import (User)


class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        if commit:
            user.save()
        return user

# class StudentSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         student = Student.objects.create(user=user)
#         student.interests.add(*self.cleaned_data.get('interests'))
#         return user


# class ProductAddForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         # fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             # 'slug': forms.SlugField(attrs={'class': 'form-control', 'placeholder': 'Subject'}),

#             'price': forms.IntegerField(attrs={'class': 'form-control', 'placeholder': 'Price'}),
#             'quantity': forms.IntegerField(attrs={'class': 'form-control', 'placeholder': 'Price'}),
#             'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'photo': forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'category': forms.ChoiceField(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'published_at': forms.DateTimeField(attrs={'class': 'form-control', 'placeholder': 'Title'}),

#             # 'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
#         }
#         exclude = ['user']
# class ProductAddForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         # fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(),
#             # 'slug': forms.SlugField(attrs={'class': 'form-control', 'placeholder': 'Subject'}),

#             'price': forms.IntegerField(),
#             'quantity': forms.IntegerField(),
#             'description': forms.TextInput(),
#             'photo': forms.ImageField(),
#             'category': forms.ChoiceField(),
#             'published_at': forms.DateTimeField(),

#             # 'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
#         }
#         exclude = ['user']