from pathlib import Path
def read(): # beolvassa az adatbázisból az összes sort és a kijelölt (fontosnak tartott) oszlopokat
    scanned = []                          
    p = Path(__file__).with_name('gyartastervezes_csv3.csv')
    with p.open('r',encoding="utf-8") as file:
        content = file.readlines()
        for row in content:
            row = row.strip()
            column = row.split(";")
            data = {"assembly":column[1], "length":column[5], "width": column[7], "project_id": column[13]}
            scanned.append(data)  
    return scanned         

def select (input, a, b): # kiválasztja a beolvasott adatbázisból a kelyheket assembly alapján
    output = []
    for i in range(1,len(input)):
        data = input[i]
        assembly = data["assembly"]
        num = True
        for char in assembly:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num = False
        if num:
            assembly = int(assembly)
            if assembly >= a and assembly <= b:
                output.append(input[i])
    return output                 

def elemszam (input): # kigyűjti az előforduló projekteket és a gyakoriságukat
    gyakorisag = dict()
    for i in range(1,len(input)): 
        adat = input[i]
        id = adat["project_id"]
        if id not in gyakorisag: gyakorisag[id]=1
        else: gyakorisag[id]+=1
    return gyakorisag  

def sizes(input, project_id): # adott projektben adott hosszúságú és szélességű kelyhek előfordulása
    size = {}
    for i in range(1,len(input)):
        data = input[i]
        if data["project_id"] == project_id:
            s = str(data["length"]) + "x" + str(data["width"])
            if s not in size: size[s] = 1 
            else: size[s] += 1
    p = Path(__file__).with_name('meret.txt')
    with p.open('w') as file:  # Az eredményt kiírjuk a kimeneti fájlba
        file.write(str(size))     
    return size

def convert_into_matrix(_dict):
    vectors = set()
    for k,v in _dict.items():
        if k.split('x')[0] not in vectors:
            vectors.add(k.split('x')[0])
    print(list(vectors))

beolvasott = read()   
a = 1000; b = 1100
kehely = select(beolvasott, a, b)
gyakorisag = elemszam(kehely)
meret = sizes(kehely, 'P19327')

print(meret)
convert_into_matrix(meret)
