from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user_with_reader_type(self) -> None:
        User = get_user_model()
        user = User.objects.create_user(email="normal_rdr@user.com", password="foo", _type="rdr")

        # basic properties
        self.assertEqual(user.email, "normal_rdr@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        # type and type-related properties
        self.assertEqual(user._type, "rdr")
        self.assertTrue(user.allow_read)
        self.assertFalse(user.allow_update)
        self.assertFalse(user.allow_create)
        self.assertFalse(user.allow_delete)

    def test_create_user_with_owner_type(self) -> None:
        User = get_user_model()
        user = User.objects.create_user(email="normal_own@user.com", password="foo", _type="own")

        # basic properties
        self.assertEqual(user.email, "normal_own@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        # type and type-related properties
        self.assertEqual(user._type, "own")
        self.assertTrue(user.allow_read)
        self.assertTrue(user.allow_update)
        self.assertFalse(user.allow_create)
        self.assertFalse(user.allow_delete)

    def test_create_user_with_superuser_type(self) -> None:
        User = get_user_model()
        user = User.objects.create_user(email="normal_su@user.com", password="foo", _type="su")

        # basic properties
        self.assertEqual(user.email, "normal_su@user.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        # type and type-related properties
        self.assertEqual(user._type, "su")
        self.assertTrue(user.allow_read)
        self.assertTrue(user.allow_update)
        self.assertTrue(user.allow_create)
        self.assertFalse(user.allow_delete)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")

        # basic properties
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        # type and type-related properties
        self.assertEqual(admin_user._type, "su")
        self.assertTrue(admin_user.allow_read)
        self.assertTrue(admin_user.allow_update)
        self.assertTrue(admin_user.allow_create)
        self.assertFalse(admin_user.allow_delete)
            
    def test_create_user_invalid_attributes(self) -> None:
        User = get_user_model()

        # create_user missing/invalid attributes
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="email@email.com", password="foo")