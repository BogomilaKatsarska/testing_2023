from django.test import TestCase

from testing_2023.web.forms import ProfileCreateForm


class ProfileCreateFormTests(TestCase):
    def test_profile_create_form_disabled_fields__when_all__expect_all_to_be_disabled(self):
        form = ProfileCreateForm()
        disabled_fields = [
            field.widget.attrs[ProfileCreateForm.disabled_attr_name]
            for field in form.fields
        ]

        print(disabled_fields)