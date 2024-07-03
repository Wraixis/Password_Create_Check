import tkinter as tk

# Создание окна
root = tk.Tk()

# Настройки окна
root.title('Создай и проверь свой пароль')
root.geometry('500x400')
root.configure(bg='#423189')

# Добавление элементов

# Надпись
label1 = tk.Label(root, text='Создай и проверь \n свой пароль на прочность!', font='Arial, 14')
label1.pack(pady=10)
label1.config(bg='#adff2f')

label2 = tk.Label(root, text='Введите пароль: ', font='Arial, 12')
label2.pack(pady=10)

# Поле
password = tk.Entry(root)
password.pack(pady=10)

label3 = tk.Label(root, text='⏳', font='Arial, 14')
label3.pack(pady=10)

label3.config(bg='#adff2f')

# Функция - получить введенные данные + событие на кнопку
def get_value_in_input():
    entered_text = password.get()

    if len(entered_text) >= 8:
        label3.config(text='Уровень надежности: Средний 👍')
    elif len(entered_text) >= 12 and any(map(str.isdigit, entered_text)):
        label3.config(text='Уровень надежности: Высокий 👍👍')
    elif entered_text == '':
        label3.config(text='Поле пустое! Введите значение 😡')
    elif len(entered_text) < 8:
        label3.config(text='Уровень надежности: Низкий 👎')

# Кнопка
button = tk.Button(root, text='Нажми git branchменя', command=get_value_in_input)
button.pack(pady=10)

# Запуск окна
root.mainloop()