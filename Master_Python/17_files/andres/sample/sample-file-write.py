from pathlib import Path

from course.andres.sample.files.services.file_service import FileService

file_name = Path('/Users/andres/Desktop/Python/python_file.txt')
service = FileService()

service.create(str(file_name))