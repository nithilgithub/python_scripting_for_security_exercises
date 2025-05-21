# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10

print(f"{a} > {b}: {a > b}")  # False
print(f"{a} < {b}: {a < b}")  # True

# What is smaller , c or d?
c = 2.02
d = 2.01119999

print(f"{c} > {d}: {c > d}")
print(f"{c} < {d}: {c < d}")

# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957

print(f"{e} > {f}: {e > f}")
print(f"{e} < {f}: {e < f}")

# are these equal?

g = 1.02020202020
i = 1.0202020202011111

print(f"{g} == {i}: {g == i}")