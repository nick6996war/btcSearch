# -*- coding: utf-8 -*-

from distutils.log import error
import io
import os
import textract
import re


# можно юзать что угодно пока так для удобства разработки
fileTypes = [".xlsx", ".docx"]
# счетчик файлов
counter = 0

pathnameinp = input("Input path: ")
if not pathnameinp:
    fileNameOut = r"C:\\"
else:
    fileNameOut = str(pathnameinp)

# функция сбора путей к файла и записи их в файл ТК либо я не вьехал в питон либо он не дружит со сложной рекурсией
thisdir = os.getcwd()
with io.open("pathFile.txt", "w", encoding="utf-8", errors='ignore') as pathFile:
    # во второй ревизии будет интерфейс и можно будет с консоли прописывать диск или путь
    for r, d, f in os.walk(fileNameOut):  # change the hard drive, if you want
        for file in f:
            filepath = os.path.join(r, file)
            if os.path.splitext(file)[1] in fileTypes:
                counter += 1
                pathFile.write(os.path.join(r, file) + "\n")
                # print(os.path.join(r, file), os.path.splitext(file))
pathFile.close()


with io.open("words.txt1", 'r', encoding='utf8', errors='ignore') as wordsF:
    wordList = wordsF.read().splitlines()
wordsF.close()

counteWords = 0
# функция чтения путей по к файлам
try:
    print(f"All: {counter} files.")
    with io.open("pathFile.txt", 'r', encoding='utf8', errors='ignore') as f:
        pathText = f.read().splitlines()
        for path in pathText:
            textfile = textract.process(path)
            # print (textfile)
            for word in wordList:
                if bytes(word, 'UTF-8') in textfile:
                    seed = r"(" + word + r"(.+?)(?:\n|$|.{120}))"
                    seedMass = re.findall(seed, str(textfile))
                    #print(seed)
                    #print(seedMass[0][0])
                    counteWords += 1
                    for word2 in wordList:
                        if bytes(word2, 'UTF-8') in bytes(seedMass[0][0], 'UTF-8'):
                            counteWords += 1
                            print(str(counteWords) + " SEED-word/s in file" + path)
                        break

            counteWords = 0
except:
    print(str(error))