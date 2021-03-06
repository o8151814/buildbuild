from django.test import TestCase
from projects.models import Project, ProjectWaitList
from teams.models import Team
from users.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class ProjectWaitList_test(TestCase):
    def setUp(self):
        self.project_name = "Team1"
        self.second_team_name = "Second Team"
        self.project_name = "Project1"
        self.second_project_name = "Second Project"

        self.team = Team.objects.create_team(
            name = self.project_name
        )

        self.second_team = Team.objects.create_team(
            name = self.second_team_name
        )

        self.project = Project.objects.create_project(
            name = self.project_name
        )

        self.second_project = Project.objects.create_project(
            name = self.second_project_name
        )
       
        self.project_wait_list = ProjectWaitList.objects.create_project_wait_list(
            project = self.project,
            team = self.team,
        )
 
# Attribute
    def test_project_wait_list_must_have_date_requested(self):
        try:
            self.project_wait_list.date_requested
        except AttributeError:
            self.fail("team wait_list should have date_requested")

# Validation
    def test_create_project_wait_list_project_argument_should_be_Project_object(self):
        try:
            self.project_wait_list = ProjectWaitList.objects.create_project_wait_list(
                self.team,
                self.team,
            )
        except ValidationError:
            pass

    def test_create_project_wait_list_team_argument_should_be_Team_object(self):
        try:
            self.project_wait_list = ProjectWaitList.objects.create_project_wait_list(
                self.project,
                self.project,
            )
        except ValidationError:
            pass

