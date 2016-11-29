from selenium import webdriver

outputdir = "../log/"
service_log_path = "{}/chromedriver.log".format(outputdir)
service_args = ['--verbose']

chromeDriverPath = "C:\\Users\\animeshb\\AppData\\Local\\Continuum\\Anaconda\\chromedriver.exe"
browser = webdriver.Chrome(executable_path = chromeDriverPath,
                           service_args=service_args,
                        service_log_path=service_log_path)

url = 'http://selenium-python.readthedocs.org/en/latest/getting-started.html'
browser.get(url)