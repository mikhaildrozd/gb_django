from authapp.models import ShopUser
from authapp.form import ShopUserUpdateForm


class ShopUserAdminEditForm(ShopUserUpdateForm):
    class Meta:
        model = ShopUser
        fields = '__all__'