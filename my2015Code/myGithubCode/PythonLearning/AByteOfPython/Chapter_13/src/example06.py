# encoding=utf-8
import io
f = io.open("../data/myData.data",'wt',encoding="utf-8")
f.write(u"Imageinge a norwegiean language")
f.close()

text = io.open("../data/myData.data", encoding="utf-8").read()

print text