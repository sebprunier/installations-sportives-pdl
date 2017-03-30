class Activity:
	def __init__(self, code, label):
		self.code = code
		self.label = label

	def __repr__(self):
		return "{} - {}".format(self.code, self.label)
