import os, platform, logging

if platform.platform().startswith('Windows'):	
	logFile = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'),"test.log")
else:
	logFile = os.path.join(os.getcwd(),"../log/test.log")

print "Logging To:->>>>", logFile

logging.basicConfig(
	level=logging.DEBUG,
	format = '%(asctime)s : %(levelname)s : %(message)s',
	filename = logFile,
	fileMode = 'w',)

logging.debug("Start")
logging.info("Doing SOmething")
logging.warning("Dying Now")