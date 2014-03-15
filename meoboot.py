import sys, os, struct

def MeobootMainEx(source, target, installsettings):
	
	meohome = "/media/meoboot"
	meoroot = "media/meoboot"
	
	rc = os.system("init 2")
	cmd = "showiframe /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/icons/meoboot.mvi > /dev/null 2>&1"
	rc = os.system(cmd)
	
	to = "/media/meoboot/MbootM/" + target
	cmd = "rm -r %s > /dev/null 2<&1" % (to)
	rc = os.system(cmd)
	
	to = "/media/meoboot/MbootM/" + target
	cmd = "mkdir %s > /dev/null 2<&1" % (to)
	rc = os.system(cmd)
	
	
	to = "/media/meoboot/MbootM/" + target
	cmd = "chmod -R 0777 %s" % (to)
	rc = os.system(cmd)
	
	rc = MeobootExtract(source, target)
	
	
	
  	cmd = "mkdir -p %s/MbootM/%s/media > /dev/null 2>&1" % (meohome, target)
	rc = os.system(cmd)
  	cmd = "rm %s/MbootM/%s/%s > /dev/null 2>&1" % (meohome, target, meoroot)
	rc = os.system(cmd)
  	cmd = "rmdir %s/MbootM/%s/%s > /dev/null 2>&1" % (meohome, target, meoroot)
	rc = os.system(cmd)
  	cmd = "mkdir -p %s/MbootM/%s/%s > /dev/null 2>&1" % (meohome, target, meoroot)
	rc = os.system(cmd)
	
# Netw e pass	
	cmd = "cp /etc/network/interfaces %s/MbootM/%s/etc/network/interfaces > /dev/null 2>&1" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp /etc/passwd %s/MbootM/%s/etc/passwd > /dev/null 2>&1" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp /etc/resolv.conf %s/MbootM/%s/etc/resolv.conf > /dev/null 2>&1" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp /etc/wpa_supplicant.conf %s/MbootM/%s/etc/wpa_supplicant.conf > /dev/null 2>&1" % (meohome, target)
	rc = os.system(cmd)
	

# MeoBoot copy itself and settings (because the image in multiboot load our kernel we need to copy our kernel modules too)
	cmd = "cp -r /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot %s/MbootM/%s/usr/lib/enigma2/python/Plugins/Extensions" % (meohome, target)
	rc = os.system(cmd)
	cmd = "rm -r %s/MbootM/%s/lib" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp -r /lib  %s/MbootM/%s/" % (meohome, target)
	rc = os.system(cmd)
	cmd = "rm  %s/MbootM/%s/etc/rc3.d/S20usbtunerhelper" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp /usr/bin/usbtuner %s/MbootM/%s/usr/bin" % (meohome, target)
	rc = os.system(cmd)
	cmd = "cp /etc/init.d/usbtuner %s/MbootM/%s/etc/init.d" % (meohome, target)
	rc = os.system(cmd)
	cmd = "ln -s %s/MbootM/%s/etc/init.d/usbtuner %s/MbootM/%s/etc/rc3.d/S20usbtuner" % (meohome, target, meohome, target)
	rc = os.system(cmd)


	if installsettings == "True":
		cmd = "mkdir -p %s/MbootM/%s/etc/enigma2 > /dev/null 2>&1" % (meohome, target)
		os.system("mv /etc/enigma2/skin_user.xml /etc/enigma2/skin_user.bhm")
		rc = os.system(cmd)
		cmd = "cp -f /etc/enigma2/* %s/MbootM/%s/etc/enigma2/" % (meohome, target)
		rc = os.system(cmd)
		cmd = "cp -f /etc/tuxbox/* %s/MbootM/%s/etc/tuxbox/" % (meohome, target)
		rc = os.system(cmd)
		os.system("mv /etc/enigma2/skin_user.bhm /etc/enigma2/skin_user.xml")

# Meoboot be sure mountpoint exists
#	cmd = "mkdir -p %s/MbootM/%s/media > /dev/null 2>&1" % (meohome, target)
#	rc = os.system(cmd)
#	cmd = "mkdir -p %s/MbootM/%s/media/usb > /dev/null 2>&1" % (meohome, target)
#	rc = os.system(cmd)

#	filename = meohome + "/MbootM/" + target + "/etc/fstab"
#	filename2 = filename + ".tmp"
#	out = open(filename2, "w")
#	f = open(filename,'r')
#	for line in f.readlines():
#		if line.find('/dev/mtdblock2') != -1:
#			line = "#" + line
#		elif line.find('/dev/root') != -1:
#			line = "#" + line
#		out.write(line)
#	f.close()
#	out.close()
#	os.rename(filename2, filename)
	
	
#boot mount hack	
#	mypath = meohome + "/MbootM/" + target +  "/usr/lib/ipkg/info/"
#	for fn in os.listdir(mypath):
#        	if fn.find('kernel-image') != -1:
#			if fn.find('postinst') != -1:
#				filename = mypath + fn
#				filename2 = filename + ".tmp"
#				out = open(filename2, "w")
#				f = open(filename,'r')
#				for line in f.readlines():
#					if line.find('/boot') != -1:
#						line = line.replace("/boot", "/boot > /dev/null 2>\&1; exit 0")
#					out.write(line)
#				f.close()
#				out.close()
#				os.rename(filename2, filename)
#				cmd = "chmod -R 0755 %s" % (filename)
#				rc = os.system(cmd)
#		if fn.find('-bootlogo.postinst') != -1:
#			filename = mypath + fn
#			filename2 = filename + ".tmp"
#			out = open(filename2, "w")
#			f = open(filename,'r')
#			for line in f.readlines():
#				if line.find('/boot') != -1:
#					line = line.replace("/boot", "/boot > /dev/null 2>\&1; exit 0")
#				out.write(line)
#			f.close()
#			out.close()
#			os.rename(filename2, filename)
#			cmd = "chmod -R 0755 %s" % (filename)
#			rc = os.system(cmd)
#		if fn.find('-bootlogo.postrm') != -1:
#			filename = mypath + fn
#			filename2 = filename + ".tmp"
#			out = open(filename2, "w")
#			f = open(filename,'r')
#			for line in f.readlines():
#				if line.find('/boot') != -1:
#					line = line.replace("/boot", "/boot > /dev/null 2>\&1; exit 0")
#				out.write(line)
#			f.close()
#			out.close()
#			os.rename(filename2, filename)
#			cmd = "chmod -R 0755 %s" % (filename)
#			rc = os.system(cmd)
#		if fn.find('-bootlogo.preinst') != -1:
#			filename = mypath + fn
#			filename2 = filename + ".tmp"
#			out = open(filename2, "w")
#			f = open(filename,'r')
#			for line in f.readlines():
#				if line.find('/boot') != -1:
#					line = line.replace("/boot", "/boot > /dev/null 2>\&1; exit 0")
#				out.write(line)
#			f.close()
#			out.close()
#			os.rename(filename2, filename)
#			cmd = "chmod -R 0755 %s" % (filename)
#			rc = os.system(cmd)
#		if fn.find('-bootlogo.prerm') != -1:
#			filename = mypath + fn
#			filename2 = filename + ".tmp"
#			out = open(filename2, "w")
#			f = open(filename,'r')
#			for line in f.readlines():
#				if line.find('/boot') != -1:
#					line = line.replace("/boot", "/boot > /dev/null 2>\&1; exit 0")
#				out.write(line)
#			f.close()
#			out.close()
#			os.rename(filename2, filename)
#			cmd = "chmod -R 0755 %s" % (filename)
#			rc = os.system(cmd)	

	
	filename = meohome + "/MbootM/" + target + "/.meoinfo"
	out = open(filename, "w")
	out.write(target)		
	out.close()


	mypath = meohome + "/MbootM/" + target + "/var"
	if os.path.isdir(mypath):
		filename = meohome + "/MbootM/.meoboot"
		out = open(filename, "w")
		out.write(target)		
		out.close()

	rc = os.system("sync")
	os.system("reboot")
 
def MeobootExtract(source, target):
	
	for i in range(0, 20):
		mtdfile = "/dev/mtd" + str(i)
		if os.path.exists(mtdfile) is False:
			break
	mtd = str(i)
	
	if os.path.exists("/media/meoboot/ubi") is False:
		rc = os.system("mkdir /media/meoboot/ubi")
	
	sourcefile = "/media/meoboot/MbootUpload/%s.zip" % (source)
	if os.path.exists(sourcefile) is True:
		os.chdir("/media/meoboot/MbootUpload")
   		rc = os.system("unzip " + sourcefile)
	else:
   		return 0
		
	rc = os.system("rm " +  sourcefile)
	os.chdir("vuplus")
	
	rootfname = "root_cfe_auto.jffs2"
	
	if os.path.exists("./ultimo") is True:
		os.chdir("ultimo")
	elif os.path.exists("./uno") is True:
		os.chdir("uno")
	elif os.path.exists("./duo") is True:
		os.chdir("duo")
	elif os.path.exists("./solo") is True:
		os.chdir("solo")
	elif os.path.exists("./solo2") is True:
		os.chdir("solo2")
		rootfname = "root_cfe_auto.bin"
	elif os.path.exists("./duo2") is True:
		os.chdir("duo2")
		rootfname = "root_cfe_auto.bin"
		
	rc = os.system("modprobe nandsim cache_file=/media/meoboot/image_cache first_id_byte=0x20 second_id_byte=0xaa third_id_byte=0x00 fourth_id_byte=0x15")
	cmd = "dd if=%s of=/dev/mtdblock%s bs=2048" % (rootfname, mtd)
	rc = os.system(cmd)
	cmd = "ubiattach /dev/ubi_ctrl -m %s -O 2048" % (mtd)
	rc = os.system(cmd)
	rc = os.system("mount -t ubifs ubi1_0 /media/meoboot/ubi")
	
	os.chdir("/home/root")
	rc = os.system("rm -r /media/meoboot/MbootUpload/vuplus")
	
	cmd = "cp -r /media/meoboot/ubi/* /media/meoboot/MbootM/" + target
	rc = os.system(cmd)
	rc = os.system("umount /media/meoboot/ubi")
	cmd = "ubidetach -m %s" % (mtd)
	rc = os.system(cmd)
	rc = os.system("rmmod nandsim")
	rc = os.system("rm /media/meoboot/image_cache")
		
	return 1

