from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError




class ShopUser(AbstractUser):
    def validate_image(avatar):
        filesize = avatar.__sizeof__()
        megabyte_limit = 1.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    age = models.PositiveIntegerField(verbose_name='возраст', null=True, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар', validators=[validate_image])
    sity = models.CharField(max_length=40, db_index=True, blank=True, verbose_name="Город")
    # phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name="Телефон")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('email',)
