from django.test import TestCase 
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
# Write your tests here.

class InventoryConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = settings.SECRET_KEY
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Bad Secret key: {e.messages}"
            self.fail(msg)