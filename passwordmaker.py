#Password_Master_G&R
# ver: 1.0





import string
import random
import hashlib


def step_define(num):                                                                                               #определяем количество шагов 1 и шагов 2
    step_1 = num // 4
    step_2 = num % 4
    return step_1, step_2


def choose_sym():                                                                                                #выбираем из какого множества берем символ
    return random.randint(1,3)


def step_1_gen(step_1, rules):                                                                                  #генерируем шаг_1
    s = ''
    s += random.choice(rules['letters'])
    s += str(random.randint(0,9))
    s += random.choice(rules['letters'])
    s += random.choice(rules['spec_sym'])
    return s


def step_2_gen(rules):                                                                                       # генерируем шаг_2, используя выбор множества, описанный выше
    s = ''
    if choose_sym() == 1:
      s += random.choice(rules['letters'])
    elif choose_sym() == 2:
      s += str(random.randint(0,9))
    else:
      s += random.choice(rules['spec_sym'])
    return s


letters = list(string.ascii_lowercase)+ list(string.ascii_uppercase)                                             # Большие + маленькие символы
spec_sym = ['-','_','!','@','%','#','?','&']
rules = {'letters':letters,'spec_sym':spec_sym}

def create_hash(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()

'''def print_to_file(password):                                                                                      # Генерирует hash пароля и выводит его в файл (базу паролей)
  passwords = open('H_F_P_M.txt', 'a')
  passwords.write(create_hash(password) +"\n")
  passwords.close()

import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RAISED, borderwidth=1, bg="white")
frame.grid()


# Recovery part code
label_rec = tkinter.Label(frame, text="Введите пароль для проверки", font="Arial 13", bg="white" )
label_rec.grid_remove()
passwd_to_check = tkinter.Entry(frame, width=40, font="16")
passwd_to_check.grid_remove()
is_in_base_1 = tkinter.Label(frame, text="Верный пароль", font="Arial 18", bg="white")
is_in_base_2 = tkinter.Label(frame, text="Неверный пароль", font="Arial 18", bg="white")
is_in_base_1.grid_remove()
is_in_base_2.grid_remove()


def check_hash(password):
    file = open('H_F_P_M.txt', 'r')
    password_base = file.read()
    password_base = password_base.split("\n")
    file.close()
    for x in password_base:
        if x == create_hash(password):
            return True
    return False


def print_is_in_base(password):
    passwd_TO_CHECK = str(passwd_to_check.get())
    if check_hash(passwd_TO_CHECK) == True:
        is_in_base_1.grid()
        is_in_base_2.grid_remove()
    else:
        is_in_base_1.grid_remove()
        is_in_base_2.grid()
    

            
check_button = tkinter.Button(frame,text="Проверить",
                        width=10,
                        height=1,                                                                                         #ширина и высота
                        bg="white",fg="black",                                                                            #цвет фона и надписи
                          font="Arial 16",
                         compound=CENTER) 

check_button.bind("<Button-1>", print_is_in_base)
check_button.grid_remove()


#Text about programm
tap_1 = "Эта программа создана учеником 9Б класса МОУ гимназии №3 Максимовым Денисом."
tap_2 = "Программа состоит из двух разделов, между которыми можно переключаться, выбирая соответсвующие пункты меню:"
tap_3 = ">>> Создание"
tap_4 = "Для создания пароля:"
tap_5 = "Выберите длину пароля, перетаскивая ползунок на шкале (от 6 до 32 символов)"
tap_6 = "Нажмите кнопку Создать"
tap_7 = "В окне ниже появится сгенерированный пароль"
tap_8 = ">>> Восстановление"
tap_9 = "Для восстановления пароля:"
tap_10 = "Введите пароль, который помните, в строку"
tap_11 = "Нажмите кнопку Проверить"
tap_12 = "В строке ниже появится сообщение."
tap_13 = "Если пароль неверный, продолжайте перебор, пока не появится сообщение о том, что пароль верный"
text_about_programm = tap_1 + "\n" + "\n" + tap_2 + "\n" + "\n" + tap_3 + "\n" + "\n" + tap_4 + "\n" + tap_5 + "\n" + tap_6 + "\n" + tap_7 + "\n" + "\n" + tap_8 + "\n" + "\n" + tap_9 + "\n" + tap_10 + "\n" + tap_11 + "\n" + tap_12 + "\n" + tap_13
label_about_prog = tkinter.Label(frame, text=text_about_programm, font="Arial 12", bg="white" )
label_about_prog.grid_remove()


def recovery_part():
    label_rec.grid()
    passwd_to_check.grid()
    check_button.grid()
    label_pw_len.grid_remove()
    len_Scale.grid_remove()
    gen_button.grid_remove()
    label_2_pw.grid_remove()
    pass_pr.grid_remove()
    label_about_prog.grid_remove()
    is_in_base_1.grid_remove()
    is_in_base_2.grid_remove()

    
def about_programm():
    label_about_prog.grid()
    label_rec.grid_remove()
    passwd_to_check.grid_remove()
    check_button.grid_remove()
    label_pw_len.grid_remove()
    len_Scale.grid_remove()
    gen_button.grid_remove()
    label_2_pw.grid_remove()
    pass_pr.grid_remove()
    is_in_base_1.grid_remove()
    is_in_base_2.grid_remove()

    
def back_to_generation():
    label_rec.grid_remove()
    passwd_to_check.grid_remove()
    check_button.grid_remove()
    label_about_prog.grid_remove()
    label_pw_len.grid()
    len_Scale.grid()
    gen_button.grid()
    label_2_pw.grid()
    pass_pr.grid()
    is_in_base_1.grid_remove()
    is_in_base_2.grid_remove()
    

    
m = tkinter.Menu()                                                                                                    # Создаем меню и привязываем к нему функции
tk.config(menu=m)
fm = tkinter.Menu(m)
m.add_cascade(label="Меню", menu=fm)
fm.add_command(label="Создание", command=back_to_generation)
fm.add_command(label="Восстановление", command=recovery_part)
fm.add_command(label="О программе", command=about_programm)

label_pw_len = tkinter.Label(frame, text="Выберите длину пароля", font="Arial 13",bg="white" )
label_pw_len.grid()
list_len = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23","24", "25", "26", "27", "28", "29", "30", "31", "32"]
len_Scale = tkinter.Scale(frame,orient=HORIZONTAL,length=640,
          from_=6,to=32,tickinterval=1,resolution=1,bg="white")
len_Scale.grid()
'''

def password_creator():
    s = 10
    step_1, step_2 = step_define(s)
    password = ''
    for i in range(step_1):
        password += step_1_gen(step_1, rules)
    for i in range(step_2):
        password += step_2_gen(rules)
    return password

'''
g_password = password_creator()        
def password_printer(event):                                                                                           #Генерирует и выводит пароль
    password = password_creator()
    print_to_file(password)
    pass_pr.delete(1.0,END)
    pass_pr.insert(END, password)'''

        
'''gen_button = tkinter.Button(frame,text="Создать",
                        width=10,
                        height=1,                                                                                         #ширина и высота
                        bg="white",fg="black",                                                                            #цвет фона и надписи
                          font="Arial 16",
                         compound=CENTER)                                                  


label_2_pw = tkinter.Label(frame, text="Ваш пароль:", font="Arial 16", bg="white")
label_2_pw.grid()

pass_pr = tkinter.Text(frame, width=40, height=1, font="20", wrap=WORD)
pass_pr.grid()

for_pw = (str(pass_pr))
global g_password
gen_button.bind("<Button-1>", password_printer)
gen_button.grid()
              
tk.mainloop()'''

# Made by Denis Maksimov. Gymnasium №3. 2016





