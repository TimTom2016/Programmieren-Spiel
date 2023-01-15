import src.commandHelper as commandHelper

class Loop:
	def __init__(self, Controller):
		self.Controller = Controller
		self.commands = [[]]
	def addCommand(self, command,args):
		self.commands.append([command,args])
	def execute(self):
		for command in self.commands:
			self.Controller.Interpreter.executeCommand(command[0],command[1])
		return

class ForLoop(Loop):
	def __init__(self, Controller, args):
		self.Controller = Controller
		self.commands = [[]]
		self.args = args
		self.iterations = 0
		self.parseArgs()
	def parseArgs(self):
		self.iterations = int(self.args[0])
	def execute(self):
		for i in range(self.iterations):
			for command in self.commands:
				self.Controller.Interpreter.executeCommand(command[0],command[1])
		return






class Interpreter:
	def __init__(self, Controller):
		self.Controller = Controller
		self.commands = {}
		self.loadCommands()

	def loadCommands(self):
		self.commands = commandHelper.commands()

	def identifyCommand(self, command):
		if command in self.commands:
			return self.commands[command]
		else:
			return None
	def parseArgs(self, args):
		return args.split(",").strip(" ")

	def executeCommand(self, command, args):
		cmd = self.identifyCommand(command)
		if cmd:
			cmd(self.Controller, self.parseArgs(args))
		else:
			self.Controller.Logger.log("ERROR","Command not found: " + command)
		return

	def getIndent(self, line):
		indent = 0
		for char in line:
			if char == "\t":
				indent += 1
			else:
				return indent
		return indent
	def getSpaces(self, line):
		spaces = 0
		for char in line:
			if char == " ":
				spaces += 1
			else:
				return spaces
		return spaces

	