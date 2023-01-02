import re
def getNumbers(str):
    array = re.findall(r'[0.0-9]+', str)
    return array

str="Вася Пупкин 123456 Температура у больного 36.6 Завтра на улице-5 градусовю Число пи равно-3.14159265358979323846 у Буратино было 2 яблока и 3.5 из них он съел"
array=getNumbers(str)
print(*array)