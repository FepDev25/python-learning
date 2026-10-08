import platform
import sys
import locale

system = platform.system()
print(system)

version = platform.version()
print(version)

print(platform.python_version())
print(platform.uname())
print(platform.machine())
print(platform.processor())

print(sys.version)
print(sys.platform)
print(sys.executable)
print(sys.getdefaultencoding())
print(locale.getlocale())
print(locale.getencoding())

object_str = 'Hola que tal'

print(sys.getsizeof(object_str))
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(sys.argv[6])

print(f'Script Name: {sys.argv[0]}')
if len(sys.argv) > 1:
    print('Primer argumento', sys.argv[1])
if len(sys.argv) > 2:
    print('Segundo argumento: ', sys.argv[2])