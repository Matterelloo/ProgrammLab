class CSVFile():
  def __init__(self, name):
    try:
      file = open(name, 'r')
    except FileNotFoundError:
      print("Il file non esiste")
      
    self.nome = name

  def get_data(self):
    file = open(self.name, 'r')
    righe = []
    for riga in file:
      dati_riga = riga.split(',')
      righe.append(dati_riga)
    file.close()

    return righe

csv_file = CSVFile('./shampoo_salaes.txt')
