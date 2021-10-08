#for bot's function
class bot_function:
	list_of_commands = {None:None, }
	def __init__(self, name, permissions, desc_ov, desc_main, use):
		self.name = name
		self.permissions = permissions
		self.desc_ov = desc_ov
		self.desc_main = desc_main
		self.use = use
		bot_function.list_of_commands[name] = self


	def get_name(self):
		return self.name
	def get_permissions(self):
		return self.permissions
	def get_desc_ov(self):
		return self.desc_ov
	def	get_desc_main(self):
		return self.desc_main
	def get_use(self):
		return self.use
