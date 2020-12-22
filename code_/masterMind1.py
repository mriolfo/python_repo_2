# refactor folder name code to code_ because of the debug is not working if detect
# reserved words

n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))
n3 = int(input("Third Number: "))

print(
    "MAX: {} and MIN: {}".format(
        max(n1, n2, n3), min(n1, n2, n3)
    )
)

f = int(input("F: "))
c = int((f - 32) * 5 / 9)

print("F: {} is C: {}".format(f, c))
