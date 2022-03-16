import numpy as np
from pathlib import Path


def read():
    p = Path(__file__).with_name('gyartastervezes_csv3.csv')
    with p.open('r', encoding="utf-8") as file:
        content = file.readlines()
        scanned = np.zeros((len(content), 5)).astype(str)
        for i in range(0, len(content)):
            content[i] = content[i].strip().split(";")
            data = np.array([content[i][1], content[i][5], content[i][7], content[i][10], content[i][13]])
            date = data[3].split(".")
            if len(date) == 3:
                j = 0
                for k in range(0, 3):
                    if date[k].isdigit() and int(date[k]) > 0:  j += 1
                if j == 3:
                    data[3] = np.datetime64(data[3].replace(".", "-"))
            scanned[i] = data
    return scanned


def select(input, a, b):
    output = []
    for i in range(1, len(input)):
        assembly = input[i][0]
        if assembly.isdigit() == True:
            assembly = int(assembly)
            if assembly >= a and assembly <= b:
                output.append(input[i])
    output = np.array(output)
    return output


def project(input):
    projects = dict()
    for i in range(1, len(input)):
        id = input[i][4]
        if id not in projects:
            projects[id] = 1
        else:
            projects[id] += 1
    projects = np.array(list(projects.items()))
    return projects


def sizes(input, project_id):
    size = {}
    for i in range(1, len(input)):
        if input[i][4] == project_id:
            s = str(input[i][1]) + ";" + str(input[i][2])
            if s not in size:
                size[s] = 1
            else:
                size[s] += 1
    size2 = list(size.keys())
    for j in range(0, len(size2)):
        size2[j] = size2[j].split(";")
    size2 = np.array(size2).reshape(-1, 2)
    frequency = np.array(list(size.values())).reshape(-1, 1)
    output = np.hstack((size2, frequency)).astype(float)
    p = Path(__file__).with_name('meret.txt')
    with p.open('w') as file:
        file.write(str(output))
    return output


def time(input, project_id):
    date = []
    for i in range(1, len(input)):
        if input[i][4] == project_id:
            if input[i][3] not in date:
                date.append(input[i][3])
    min = np.datetime64(date[0])
    max = np.datetime64(date[0])
    for i in range(1, len(date)):
        x = np.datetime64(date[i])
        y = np.datetime64(date[i - 1])
        if x > y:
            max = x
        elif x < y:
            min = x
    delta = max - min
    return delta

beolvasott = read()
# print(beolvasott)
a = 1000
b = 1100
kehely = select(beolvasott, a, b)
# print(kehely)
gyakorisag = project(beolvasott)
meret = sizes(kehely, 'P21138')
t = time(kehely, 'P21138')
