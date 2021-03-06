from django.test import TestCase
from teams.models import Team,WaitList
from users.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class TestWaitList(TestCase):
    def setUp(self):
        self.user_email = "test@example.com"
        self.user_password = "12345678"
        self.user_email_2 = "test2@example.com"

        self.team_name = "first_team"
        self.team_name_2 = "second_team"

        self.user = User.objects.create_user(
            email = self.user_email,
            password = self.user_password
        )

        self.team = Team.objects.create_team(
            name = self.team_name
        )

        self.user_2 = User.objects.create_user(
            email = self.user_email_2,
            password = self.user_password
        )

        self.team_2 = Team.objects.create_team(
            name = self.team_name_2
        )

        self.waitlist = WaitList.objects.create(
            team = self.team,
            wait_member = self.user,
        )
        self.waitlist.save()

    def test_team_could_get_all_waitlists(self):
        try:
            self.team.wait_members.all()
        except: 
            self.fail("getting all waitlists failed")

    def test_team_could_get_wait_member(self):
        try:
            self.team.wait_members.get_wait_member(self.user.id)
        except: 
            self.fail("getting a wait_member failed")

    def test_waitlist_must_have_date_requested(self):
        try:
            self.waitlist.date_requested
        except:
            self.fail("team waitlist must have date_requested")

