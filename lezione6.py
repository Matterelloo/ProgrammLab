class CSVFile():
  def __init__(self, nome):
    if(isinstance (nome,str)):
      file = open(nome, 'r')
    else:
      raise Exception ("Il file non esiste")
      
    self.nome = nome

  def get_data(self):
    file = open(self.nome, 'r')
    righe = []
    for riga in file:
      dati_riga = riga.split(',')
      righe.append(dati_riga)
    file.close()

    return righe

try:
  csv_file = CSVFile(2)
  except Exception as e:
      print('e')
      

