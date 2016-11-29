import os, time

# 1. File to be backed up is specified in the list.

source =['/Users/xyv/myWorks/myGithubCode']

# 2. The Backup must be stored in a main backup directory.

targetDir = '/Users/xyv/myWorks/myGithubCode/backup'

# 3. The files are backed up into a zip file
# 4. The name of zip file is current date and time.

target = targetDir + os.sep + time.strftime('%Y%m%d%H%M%S') +".zip"

# Create target directory if it is not present
if not os.path.exists(targetDir):
	os.makedir(targetDir)		# make directory

# 5. We use the zip command to put the file in a zip archive.
zipCommand = "zip -r {0} {1}".format(target,''.join(source))

print "Zip Command is:"
print zipCommand

print "Running: "

if os.system(zipCommand) ==0 :
	print "Sucessfull backup to ", target
else:
	print "Failed Backup."