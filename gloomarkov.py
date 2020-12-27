import markovify as v

with open("gloomarkov.txt") as f: t = f.read()
w = v.Text(t)
print(w.make_sentence())
