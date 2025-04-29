def generate_sequence(n):
    result = []
    current_number = 1
    while len(result) < n:
        result.extend([str(current_number)] * current_number)
        current_number += 1
    return ''.join(result[:n])


n = int(input("Введите n: "))
print(generate_sequence(n))
