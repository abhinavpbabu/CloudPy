from django.shortcuts import render
from django.conf import settings
import os
import re
import shutil
from datetime import datetime, timedelta
import time
from django.http import JsonResponse
from .utils import *
# import docker



# def run_manim_command(image_name, base_dir, user_code, class_name):
#     client = docker.from_env()
    
#     # Define the volumes
#     volumes = {
#         f"{base_dir}/manim/python_code_files": {'bind': '/mnt/code', 'mode': 'rw'},
#         f"{base_dir}/media": {'bind': '/mnt/output', 'mode': 'rw'}
#     }
    
#     # Define the command with the appropriate paths
#     docker_command = f"manim -ql /mnt/code/{user_code} -o /mnt/output/{class_name}"
    
#     try:
#         # Create and start the container
#         container = client.containers.run(
#             image_name,
#             docker_command,
#             volumes=volumes,
#             detach=True,
#             remove=True
#         )
        
#         # Wait for the container to finish and get the logs
#         container.wait()
#         logs = container.logs().decode()
#     except Exception as e:
#         return str(e)
    
#     return logs



def delete_old_files(media_dir):
    threshold_time = datetime.now() - timedelta(minutes=10)

    for root, dirs, files in os.walk(media_dir):

        #delete files that are older than 10 minutes
        for filename in files:
            filepath = os.path.join(root, filename)
            modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            if modified_time < threshold_time:
                os.remove(filepath)
                print(f'Deleted {filepath}')

        #delete files in the folder "partial_movie _files" that are older than 10 minutes
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_name == "partial_movie_files":
                for sub_root, sub_dirs, sub_files in os.walk(dir_path):
                    for sub_dir_name in sub_dirs:
                        sub_dir_path = os.path.join(sub_root, sub_dir_name)
                        sub_modified_time = datetime.fromtimestamp(os.path.getmtime(sub_dir_path))
                        if sub_modified_time < threshold_time:
                            shutil.rmtree(sub_dir_path)
                            print(f'Deleted directory {sub_dir_path}')
            else:
                # No other directory to deal with, so pass 
                pass

def save_python_code_to_file(code):
    # Define the directory where Python files will be saved
    app_dir = os.path.join(settings.BASE_DIR, 'manim')
    save_dir = os.path.join(app_dir, 'python_code_files')
    os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Generate a unique filename for the Python file
    filename = os.path.join(save_dir, 'user_code.py')

    try:
        # Write the user's Python code to the file
        with open(filename, 'w') as file:
            file.write(code)
        print('code saved as python file')
    except Exception as e:
        print(f'Failed to save file: {e}')
    
    print(f'code length:{len(code)}')

    return filename

def check_file_exists(class_name):

    media_dir = os.path.join(settings.BASE_DIR, 'media')

    png_file = os.path.join(media_dir, f"{class_name}.png")
    mp4_file = os.path.join(media_dir, f"{class_name}.mp4")

    return os.path.isfile(png_file) or os.path.isfile(mp4_file)

def find_class_name(code):
    pattern = r"class\s+(\w+)\s*\(" # example: class class_name(scene)

    for line in code.split('\n'):
        print(f"Checking line: {line}") 
        # Use regular expression to find the class name
        match = re.match(pattern, line)
        if match:
            # If a match is found, extract the class name
            class_name = match.group(1)
            print("Class name:", class_name)
            return class_name
    return "undefined"    