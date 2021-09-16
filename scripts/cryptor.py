from pyheaven import Encrypt, Decrypt, EnumFiles
import argparse
import pickle

from pyheaven.file_utils import CreateFile

def EncryptFolder(password:str=""):
	files = EnumFiles("decrypted/")
	for file in files:
		data = None
		with open("decrypted/"+file,"r") as f:
			data = f.read()
		cipher = Encrypt(pickle.dumps(data),password=password)
		CreateFile("encrypted/"+file)
		with open("encrypted/"+file,"w") as f:
			f.write(cipher)

def DecryptFolder(password:str=""):
	files = EnumFiles("encrypted/")
	for file in files:
		cipher = None
		with open("encrypted/"+file,"r") as f:
			cipher = f.read()
		data = pickle.loads(Decrypt(cipher,password=password))
		CreateFile("decrypted/"+file)
		with open("decrypted/"+file,"w") as f:
			f.write(data)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", dest="password", type=str, default='')
	parser.add_argument("--e", dest="mode", action="store_const", const='encrypt', default='decrypt')
	parser.add_argument("--d", dest="mode", action="store_const", const='decrypt', default='decrypt')
	args = parser.parse_args()
	if args.mode=='encrypt':
		EncryptFolder(args.password)
	if args.mode=='decrypt':
		DecryptFolder(args.password)
