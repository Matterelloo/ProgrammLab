class CSVFile():
  def __init__(self, name):  
    self.name = name

  def get_data(self):
    file = open(self.name, 'r')
    righe = []
    for riga in file:
      dati_riga = riga.split(',')
      righe.append(dati_riga)
    file.close()

    return righe

csv_file = CSVFile('./shampoo_sales.txt')
print(csv_file.get_data())

#"ciao, come va?" split(',') --> ['ciao', 'come va?']
