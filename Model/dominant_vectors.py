# TODO config file
# TODO correct

vector = [80, 90, 100, 120]
max_size = 600
sample_vectors = list()

def get_minimal_element():
    return min(*vector)

def get_start_vectors():
    res = list()
    for i in vector:
        temp = dict()
        for j in vector:
            temp[j] = 0
        temp[i] = max_size // i
        res.append(temp)
    for i in res:
        _i = i.copy()
        if calculate_length(_i) > max_size - get_minimal_element():
            sample_vectors.append(_i)
    return res

def get_starting_component(vector):
    for k, v in vector.items():
        if v != 0: return k

def calculate_length(vector):
    _sum = 0
    for k,v in vector.items():
        _sum += (k*v)
    return _sum

def get_fit(vector, pos):
    for key in vector.keys():
        if key == pos: continue
        length = calculate_length(vector)
        if length + key <= max_size:
            new_vect = vector.copy()
            # new_vect[k] += ((max_size - length) // k)
            new_vect[key] += 1
            get_fit(new_vect, pos)
            if new_vect not in sample_vectors and calculate_length(new_vect) > \
                    (max_size - get_minimal_element()):
                sample_vectors.append(new_vect)

def get_all_combinations(vector):
    pos = get_starting_component(vector)
    while vector[pos] > 0:
        vector[pos] -= 1
        get_fit(vector.copy(), pos)

def get_sample_vectors():
    global sample_vectors

    start = get_start_vectors()
    for vector in start:
        get_all_combinations(vector)

    res = list()
    for d in sample_vectors:
        res.append(tuple(d.values()))
    return res