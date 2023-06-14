import threading
# Функция, которую будет выполнять новая нить
def print_text():
   for i in range(10):
       print("Это строка номер", i+1)
# Создаем новую нить
new_thread = threading.Thread(target=print_text)
# Запускаем новую нить
new_thread.start()
# Родительская нить также распечатывает десять строк текста
for i in range(10):
   print("Это строка номер", i+1)