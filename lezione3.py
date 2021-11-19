def somma (values):
  x=0
  for item in values:
    x=x+item
  print (x)
  return (x)

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
myfile = open('shampoo_sales.txt', 'r')
for line in myfile:
# Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
# Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
      date  = elements[0]
      value = elements[1]

# Aggiungo alla lista dei valori questo valore
      values.append(float(value))

somma(values)

# Chiudo il file
myfile.close()

