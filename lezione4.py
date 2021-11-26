class CSVFile():
  def __init__(self, nome):
    self.nome = nome

  def get_data(self):
    file = open(self.nome, 'r')
    righe = []
    for riga in file:
      dati_riga = riga.split(',')
      righe.append(dati_riga)
    file.close()

    return righe

csv_file = CSVFile('./shampoo_sales.txt')

print(csv_file.get_data())