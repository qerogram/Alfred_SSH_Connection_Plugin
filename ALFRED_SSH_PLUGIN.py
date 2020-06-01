import os, sys, subprocess

class ALFRED_SSH_MODULE :
	PATH = "" # Don't Edit Variable.
	
	# Set Environments
	LOCAL_VMWARE_FILE = ""
	VM_DEFAULT_PATH = os.environ['HOME'] + "/Virtual Machines.localized"
	
	SERVER_HOST = "ub18_2" # Server IP
	SERVER_PORT = "22" # Server PORT

	USERID = "qerogram" # User ID
	USERPW = "1234" # User PW

	def __init__(self, argv) :
		if len(argv) == 3 : self.LOCAL_VMWARE_FILE = argv[2]
		self.HOST = argv[1]
		self.PATH = argv[0][:argv[0].rfind("/")] 

	def runServer(self) :
		if self.LOCAL_VMWARE_FILE == "" : return
		os.system(f"vmrun start '{self.VM_DEFAULT_PATH}/{self.LOCAL_VMWARE_FILE}.vmwarevm/{self.LOCAL_VMWARE_FILE}.vmx' ")

	def connect(self) :
		os.system(f"{self.PATH}/Connection.sh {self.SERVER_HOST} {self.SERVER_PORT} {self.USERID} {self.USERPW}")

if __name__ == "__main__" :
	if len(sys.argv) == 2 or len(sys.argv) == 3 :
		ASM = ALFRED_SSH_MODULE(sys.argv)
		ASM.runServer()
		ASM.connect()

	else :
		print("[+] Usage : " + sys.argv[0] + " <ip>")
		print("[+] Usage : " + sys.argv[0] + " <ip> <vmx>")