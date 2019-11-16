from django.test import TestCase
from .models import MythMaker, Membership, MythMakerMembership

class TestMembershipModel(TestCase):

    def test_title_is_a_string(self):
        membership = Membership(membership_type = 'FR')
        self.assertEqual(membership.membership_type, str(membership))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Membership._meta.verbose_name_plural), 'Memberships')