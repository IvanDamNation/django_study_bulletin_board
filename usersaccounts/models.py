from django.contrib.auth.models import AbstractUser
import string
import random
from django.db import models
from django.utils import timezone  # Use only timezone with django
from django.utils.translation import gettext_lazy as _

from GameNotifPortal.const import EXP_TIME_CODE


# TODO Model for auth code
# class CodeAuth(models.Model):
#     code = models.CharField(max_length=128, unique=True)
#     exp_time = models.DateTimeField()
#
#     def generate_code(self):
#         self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
#         self.time = timezone.now() + timezone.timedelta(hours=EXP_TIME_CODE)
#         self.save()


class User(AbstractUser):
    email = models.EmailField(_('email_adress'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

#     # TODO create relation with code model
#     code_auth = models.OneToOneField(CodeAuth, on_delete=models.CASCADE)
#     # Add is activate flag for user
#     is_activated = models.BooleanField(default=False)
