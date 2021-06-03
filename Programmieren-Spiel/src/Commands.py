import os
import importlib


class Commandidentifier():
	def __init__(self,Controller):
		self.cmds = os.listdir('src/cmds')
		self.commands = ['look','move','rotate']
		self.modules = []
		self.Controller = Controller
		for i in self.cmds:
			if i == '__pycache__':
				pass
			else:
				module = importlib.import_module('src.cmds.'+i[:-3])
				self.modules.append(module)
				self.Controller.Logger.log("Loaded Command "+i[:-3])
		self.Controller.Logger.log("Loaded all Commands")
		self.Controller.Logger.log("Succesfully Initialized Command_Identifier")
	def identify(self,cmd):
		module = 0
		if cmd == "":
			self.Controller.Logger.log("Please Enter cmd")
			return
		for i in self.cmds:
			if cmd.startswith(i[:-3]):
				if cmd.find('(') != -1:
					arg = cmd[(cmd.find('(') + 1):cmd.find(')')]
					self.modules[module].execute(self.Controller.Command_helper,arg)
					self.Controller.Logger.log("Executed Command: " + i[:-3] + " and arg:" + arg)
				else:
					self.modules[module].execute(self.Controller.Command_helper)
					self.Controller.Logger.log("Executed Command: " + i[:-3] + " and arg:" + arg)
			module += 1
		self.Controller.Logger.log("Got Error in Commandidentifier")
#cmds = Commandidentifier()
#cmds.identify(Bot="",cmd="rotate")