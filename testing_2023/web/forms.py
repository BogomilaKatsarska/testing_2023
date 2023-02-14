from django import forms

from testing_2023.common.forms.mixins.disabled_form_mixin import DisabledFormMixin
from testing_2023.web.models import Profile


class ProfileCreateForm(DisabledFormMixin, forms.ModelForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Profile
        fields = '__all__'
