with open("data.txt") as file1:
    numlist = list(map(int, file1))
s = sum(numlist)
sr = s / len(numlist) if numlist else 0
ma = max(numlist) if numlist else None
mi = min(numlist) if numlist else None

with open("result.txt", "w") as file2:
    file2.write(f"Sum: {s}\n")
    file2.write(f"Arithmetic mean: {sr}\n")
    file2.write(f"Maximum: {ma}\n")
    file2.write(f"Minimum: {mi}\n")




