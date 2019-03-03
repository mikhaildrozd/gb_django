from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser
# from phonenumber_field.formfields import PhoneNumberField
import os
import random, hashlib

class ShopUserLoginForm(AuthenticationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'age', 'password1', 'password2', 'email', 'avatar', 'sity', )
        # unique_together = ('email',)

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, commit=True):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user





    # def clean_avatar(self):
    #     # print(self)
    #     avatdsfar = self.cleaned_data.get('avatar', True)
    #     # avatar = self.cleaned_data.get('avatar')
    #     print(avatdsfar)
    #     if avatar and avatar > (1 * 1024 * 1024):
    #         raise forms.ValidationError("Размер фотографии слишком большой")


    def clean_age(self):
        data = self.cleaned_data['age']
        # print(data)
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data



class ShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'age', 'password', 'email', 'first_name', 'sity', 'avatar')


    def __init__(self, *args, **kwargs):
        super(ShopUserUpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    # def clean_avatar(self):
    #     avatar = self.cleaned_data.get('avatar', False)
    #     print('fdgfdfd')
    #     if avatar and avatar._size > 1 * 1024 * 1024:
    #         raise forms.ValidationError("Размер фотографии слишком большой")
    #     return avatar

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data
