import pickle

shoplistfile = '../data/shoplist.data'

shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')

pickle.dump(shoplist,f)

f.close()

del shoplist

f = open(shoplistfile,'rb')

storedList = pickle.load(f)

print "storedList: ", storedList