from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'load necessary data in database for test'

    def handle(self, *args, **options):
        call_command('loaddata', 'division.json')
        call_command('loaddata', 'district.json')
        call_command('loaddata', 'thana.json')
        call_command('loaddata', 'post_office.json')
        call_command('loaddata', 'post_code.json')
        call_command('loaddata', 'address.json')
        call_command('loaddata', 'madrasha.json')
        call_command('loaddata', 'customUser.json')
        call_command('loaddata', 'student.json')
        call_command('loaddata', 'parent.json')
        call_command('loaddata', 'teacher.json')
        call_command('loaddata', 'skill.json')
        call_command('loaddata', 'education.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data.'))