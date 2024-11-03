def find_substring_locations(s, t):
    positions = []
    index = s.find(t)
    while index != -1:
        positions.append(index + 1)
        index = s.find(t, index + 1)
    return positions

s = "GATATATGCATATACTT"
t = "ATAT"

positions = find_substring_locations(s, t)
print(" ".join(map(str, positions))) 