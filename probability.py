def dominant_allele_probability(k, m, n):
    total = k + m + n
    
    total_pairs = total * (total - 1) / 2
    
    dominant_pairs = 0

    dominant_pairs += (k * (k - 1)) / 2  

    dominant_pairs += k * m 

    dominant_pairs += k * n 

    dominant_pairs += (m * (m - 1)) / 2 * 0.75 

    dominant_pairs += m * n * 0.5  


    probability = dominant_pairs / total_pairs
    return probability

k, m, n = 2, 2, 2
result = dominant_allele_probability(k, m, n)
print(f"{result:.5f}")  