from course.andres.sample.files.services.file_service import FileService

# file_name = 'C:\\Users\\andres\\Desktop\\Python\\python_file.txt' # Windows
file_name = '/Users/andres/Desktop/Python/python_file.txt' # Mac

service = FileService()

result = service.read(file_name)
print(result)