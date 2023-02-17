# -*- coding: utf-8 -*-
from distutils.log import error
import io
import os


# можно юзать что угодно пока так для удобства разработки
fileTypes = ["."]
# счетчик файлов
counter = 0
# 194.38.21.12
word  = "194.38.21.12" 
# pathnameinp = input("Input path: ")
# if not pathnameinp:
fileNameOut = r"C:\Users\Nikolai\Desktop\linux"
# else: 
#    fileNameOut = str(pathnameinp)

# функция сбора путей к файла и записи их в файл ТК либо я не вьехал в питон либо он не дружит со сложной рекурсией
thisdir = os.getcwd()
with io.open("pathFile.txt", "w", encoding="utf-8", errors='ignore') as pathFile:
    for r, d, f in os.walk(fileNameOut):  # change the hard drive, if you want
        for file in f:
            filepath = os.path.join(r, file)
            # if os.path.splitext(file)[1] in fileTypes:
            counter += 1
            pathFile.write(os.path.join(r, file) + "\n")
                #print(os.path.join(r, file), os.path.splitext(file))
pathFile.close()




counteWords = 0
# функция чтения путей по к файлам
print(f"All: {counter} files.")
with io.open("pathFile.txt", 'r', encoding='utf8', errors='ignore') as f:
    pathText = f.read().splitlines()
    for path in pathText:
        try:
            with io.open(path, 'r', encoding='utf8') as dataF:
                textfile = dataF.read()
            dataF.close()

            if  word in textfile: 
                #print("serched: " +path + "  word: " + word)
                counteWords +=1
                print (str(counteWords) + " search in file: " + path)

            counteWords = 0
        except:
            c =1
            print('error:' + str(error) + '\n'+ path)

