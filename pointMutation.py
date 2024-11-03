def hamming_distance(s, t):
    differences = 0
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            differences += 1
    return differences

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = hamming_distance(s, t)
print(distance)
