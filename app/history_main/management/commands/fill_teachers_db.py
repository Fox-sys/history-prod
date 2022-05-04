from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    help = "Preparing database"

    def handle(self, *args, **options):
        self.open_file()

    def open_file(self):
        with open('teachers.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))
