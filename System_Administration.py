# Use os.system() to run a Bash command

# Use subprocess.run() to run Bash commands
import os



import subprocess

subprocess.run(["ls","-l","README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
