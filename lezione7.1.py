class Model():
  def fit(self):
    raise NotImplementedError("Metodo non implementato")

  def predict(self):
    raise NotImplementedError("Metodo non implementato")

class IncrementalModel(Model):

  def predict(self, data):
    incremento = 0
    for i, item in enumerate(data):
      if(i + 1 < len(data)): incremento += data[i + 1] - item

    return data[len(data) - 1] + incremento/(len(data) - 1)


model = IncrementalModel()
print(model.predict([50, 52, 60]))


