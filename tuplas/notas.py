notas = (6,8,3,5)
print (f"As notas foram {notas}, e a maior nota foi {max(notas)}! A menor nota foi {min(notas)}!")

###############################
notes = []

for i in range (4):
    notes.append(input("Informe uma nota -> "))

t_notes = tuple(notes)

print (f"A maior nota é {max(t_notes)}!")
print (f"A menor nota é {min(t_notes)}!")