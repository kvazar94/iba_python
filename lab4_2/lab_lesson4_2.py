#Скопировать из файла F1 в файл F2 все строки, в которых нет слов,
# совпадающих с первым словом. Определить количество согласных
# букв в первой строке  файла F2.

check_lines = []
f2_lines = []
with open("F1.txt", "r") as F1:
    # итерация по строкам
    for line in F1:
        check_lines.append(line.lower())

first_word = check_lines[0].split(" ")[0]
print("Первое слово в файле F1:", first_word)


with open("F2.txt", "w") as F2:
    for line in check_lines:
        if not first_word in line:
            f2_lines.append(line)
            F2.write(line)

first_str = f2_lines[0]
consonants = 0
for i in first_str:
    if i not in 'aeiouy .,':
        consonants += 1
print("Количество согласных в первой строке файла F2:", consonants - 1)


