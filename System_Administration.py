# Use os.system() to run a Bash command

# Use subprocess.run() to run Bash commands
import os



import subprocess

subprocess.run(["ls","-l","README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
