num = int(input("What number do you want multiples of?: "))
print(f"  | {num}")
print("--------")

for i in range(0, 13):
    print(f"{i} | {i * num}")