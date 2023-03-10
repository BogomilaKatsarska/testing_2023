from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_2023.web.models import Profile


class ProfileModelTests(TestCase):
    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        # Arrange
        profile = Profile(
            name='Doncho',
            age=19,
            egn='0310230467',
        )

        # Act
        profile.full_clean() #call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_egn_has_9_digits__expect_exception(self):
        # Arrange
        profile = Profile(
            name='Doncho',
            age=19,
            egn='031023047',
        )

        # Assert
        with self.assertRaises(ValidationError) as context:
            # Act
            profile.full_clean()  # call this for validation
            profile.save()

        self.assertIsNotNone(context.exception)
