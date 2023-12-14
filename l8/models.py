class Model():
	def fit(self, data):

		raise NotImplementedError('Metodo non implementato')

	def predict(self, data):
		
		raise NotImplementedError('Metodo non implementato')


class TrendModel(Model):
	#funzione che calcola la media della variazione
	def avg_variation(self, data):
		i = 0
		sommaDif = 0
		for item in range(len(data)-1):
			sommaDif += (data[i+1] - data[i])
			i+=1
		variazione = sommaDif / i

		
	def predict(self, data):
		prev_value = None
		#for item in data:
			
		#prediction = 
		#return prediction

list=[50,52,60]
prova = TrendModel()
prova.avg_variation(list)
	

