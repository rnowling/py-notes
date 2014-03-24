class Note(object):
	def __init__(self, id, title):
		self.id = id
		self.title = title

	def to_dict(self):
		return dict(id=self.id, title=self.title)