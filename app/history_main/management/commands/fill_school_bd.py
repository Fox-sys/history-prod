from django.core.management.base import BaseCommand
from django.core.files import File
from history_main.models import Image, OutDoorSchool
import os


class Command(BaseCommand):
    help = "Preparing database"
    LOAD_FILE_DIR = 'out_door_school'

    def handle(self, *args, **options):
        folders = self.get_folder_list()[2:]
        for folder in folders:
            current_image_folder = os.path.join(self.LOAD_FILE_DIR, folder)
            school = OutDoorSchool.objects.create(name=folder)
            images = os.listdir(current_image_folder)
            for image in images:
                with open(os.path.join(current_image_folder, image), 'rb') as file:
                    dj_file = File(file)
                    im = Image.objects.create(outdoor_school=school)
                    im.image.save(image, dj_file, save=True)

    def get_folder_list(self) -> list:
        return os.listdir(self.LOAD_FILE_DIR)
