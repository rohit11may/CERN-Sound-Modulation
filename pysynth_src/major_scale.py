C_start = 40
G_start = 47
D_start = 42
A_start = 37
E_start = 44
B_start = 39
F_sharp_start = 46
F_start = 45
B_flat_start = 38
E_flat__start = 43
A_flat_start = 36
D_flat_start = 41
G_flat_start = 46



def major_scale(dictionary, key):
    general_rule = [2,2,1,2,2,2,1]
    scale = []
    start = 0
    for x in range(8):
        scale.append(dictionary[key])
        if x == 7:
            break
        else:
            key += general_rule[start]
            start += 1
    return scale
