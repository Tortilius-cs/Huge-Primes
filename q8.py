# Input values
p = int(input("Choose a prime p: "))
n = int(input("Choose a composite n: "))

# Function to generate and print sequences modulo m
def print_sequences(m):
    print("\nSequences mod", m, "\n")
    for a in range(1, m):
        seq = []
        j = 1
        value = a % m
        while j <= m or value not in seq:  # include m-th power
            if value in seq:
                break
            seq.append(value)
            j += 1
            value = pow(a, j, m)
        print(f"a = {a}: {seq}, length = {len(seq)}")

# Show sequences for prime and composite
print_sequences(p)
print_sequences(n)
