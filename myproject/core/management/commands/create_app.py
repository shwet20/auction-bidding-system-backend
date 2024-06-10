import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from time import sleep

from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

command_dir = Path(__file__).resolve().parent


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            required=True,
            help='Name of the app in the project',
        )

    def handle(self, *args, **options):
        app_name = options['name'].lower()
        app_path = os.path.join(settings.BASE_DIR, app_name)

        try:
            result = os.system('python manage.py startapp {}'.format(app_name))
            if result == 0:

                # Remove default files
                os.remove(os.path.join(app_path, 'views.py'))
                os.remove(os.path.join(app_path, 'tests.py'))

                # Read app structure config
                app_structure_file = os.path.join(
                    command_dir,
                    'app_structure.json'
                )
                app_structure = open(app_structure_file)
                app_structure = json.load(app_structure)

                # Create folders and files
                self.create_folders_with_files(app_path, app_structure)

                # Success
                self.stdout.write(
                    self.style.SUCCESS("\nApp {} created successfully".format(
                        app_name
                    ))
                )
                self.stdout.write(
                    "{} Add the '{}' app to your settings.py file in BUSINESS_APPS=[]\n".format(
                        self.style.WARNING("Note:"), app_name
                    )
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR("Failed to create app - {}! Check below error info:".format(
                    app_name
                ))
            )
            print("Error: {}".format(e))
            shutil.rmtree(app_path)

    def create_folders_with_files(self, app_path, app_structure):
        try:
            for folder, files in app_structure.items():

                # Create folder
                self.stdout.write(
                    "\n> Setting up {} directory".format(
                        self.style.SUCCESS(folder)
                    )
                )
                test_folder_path = os.path.join(app_path, folder)
                os.makedirs(test_folder_path)

                # Create files in folder
                pbar = tqdm(files.items())
                for file_name, file_content in pbar:
                    sleep(0.10)
                    pbar.set_description("Creating {}".format(file_name))
                    clock = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

                    with open(os.path.join(test_folder_path, file_name), "w") as f:
                        f.write("# File created at {}".format(clock))
                        f.write(file_content)
                        f.write("\n")
                pbar.close()

        except Exception as e:
            raise Exception(e)
