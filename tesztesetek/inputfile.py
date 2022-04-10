import numpy as np
from pathlib import Path

def read(): # beolvassa a fájlt                       
    p = Path(__file__).with_name('info.txt')
    with p.open('r',encoding="utf-8") as file:
        content = file.readlines()
        for i in range (0, len(content)):
            content[i] = content[i].strip().split(",")
        n = int(content[0][0]) # darabszám
        length = content[1]
        width = content[2]
        matrix = np.zeros([len(length)*len(width), 3])
        for i in range(0, len(length)):
            for j in range(0, len(width)):
                matrix[i*len(width)+j, 0] = length[i]
                matrix[i*len(width)+j, 1] = width[j]
                matrix[i*len(width)+j, 2] = n
        p = Path(__file__).with_name('input.txt')
        with p.open('w') as file:
            file.write(str(matrix))  # length, width, gyakorisag   
    return matrix

print(read())
