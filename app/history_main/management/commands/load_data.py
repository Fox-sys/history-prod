from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
from ...models import SolderPost, Tag
from string import ascii_letters
from ...forms import SearchForm
from random import choice
import json
import os
from pathlib import Path

class Command(BaseCommand):
    help = "loading prepared data"

    def handle(self, *args, **kwargs):
        print(Path(__file__).resolve().parent.parent)
        for i in os.listdir('data'):
            path = f'data/{i}/'
            info = self.get_info(path)
            photo = self.get_pic(path)
            desc = self.get_desc(path)
            form = SearchForm({"info": info['tags']})
            if form.is_valid():
                tags = form.get_tags()
            else:
                raise Exception(f"file 'info.json' in {i} isn't valid, please check 'tags' field")
            post = SolderPost.objects.create(
                first_name=info["name"],
                middle_name=info["middle_name"],
                last_name=info["last_name"],
                desc=desc,
                birth_date=info["birth_date"],
                death_date=info["death_date"],
                is_alive=info["is_alive"],
                photo=photo
            )
            for j in tags:
                post.tags.add(j)
            post.save()

    def get_info(self, path):
        with open(path+"info.json", "r") as read_file:
            data = json.load(read_file)
            return data

    def get_pic(self, path):
        with open(path+"photo.jpg", "rb") as read_file:
            photo = SimpleUploadedFile(''.join(choice(ascii_letters) for i in range(25)) + ".jpg", content=read_file.read(), content_type='image/jpg')
            return photo

    def get_desc(self, path):
        with open(path+"text.txt", "r") as read_file:
            return read_file.read()