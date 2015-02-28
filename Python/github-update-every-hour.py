import subprocess
import time
## dd/mm/yyyy format
# date = time.strftime("%d/%m/%Y")
def console_output(subprocess):
	"""
	@param subprocess object of type 'subprocess'
	@return s string representation of console output
	"""
	s = ""
	for line in subprocess.stdout.readlines():
		s += line
	return s
def changes_made(console_string):
	"""
	@param console_string String
	@return chg (boolean) True if string says there's nothing to commit.
	"""
	chg = "nothing to commit, working directory clean" in console_string
	return (not chg)
if __name__ == '__main__':
	"""
	git pulls, adds., commits and pushes to repository under the default/current credentials.
	"""
	commands = ["git pull",
		"git status",
		"git add .",
		"git commit -m \"data update\"",
		"git push -u origin master"]
	for string in commands:
		p = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		print(string) #your command
		console_str = console_output(p) #command output
		print(console_str)
		if changes_made(console_str):
			pass
		else:
			break
	time.sleep(3600) # try again later (in an hour)
	print("I'll try again in an hour")
