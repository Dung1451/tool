import os, sys, time, datetime,  json, requests, re
#màu
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
f = """------------------------------------------------------------"""
banner = """
\033[1;96m██████╗  [•] Copyright Axeyed Kha (có của Dũng nữa :))
\033[1;92m██╔══██╗ [•] Tool tính đủ thứ trên đời :v
\033[1;95m██║  ██║ [•] Facebook: Dũng Dũng
\033[1;92m██║  ██║ [•] Phiên bản v1.0
\033[1;96m██████╔╝ [•] Zalo: 0936485851
\033[1;97m╚═════╝  [•] Chúc các bạn dùng tool vui vẻ
"""
def write(z):
  for e in z + '\n':
    sys.stdout.write(e) 
    sys.stdout.flush()
    time.sleep(0.01)
def menu():
  os.system('clear')
  print(banner) 
  write(f) 
  write("chào mừng tới tool tds token v1.0 by Dũng")
  print(xb+"mời chọn 1 job để chạy ")
  print(f) 
  time.sleep(0.1)
  write("[1]Like")
  write("[2]Follow")
  write("[3]Reaction")
  write("[4]Comment")
  nhap = input("nhập job muốn chạy: ")
  if nhap == '1' or nhap == '01':
    tool_like_function()
  elif nhap == '2' or nhap == '02':
    tool_follow_function()
  elif nhap == '3' or nhap == '03':
    tool_reaction_function()
  elif nhap == '4' or nhap == '04':
    tool_cmt_function()
  else:
    print(d+"Nhập sai!")
    time.sleep(3)
    os.system('clear')
#tool Like 
def tool_like_function():
  os.system('clear')
  print(banner)
  print(f)
  print(v+"Job bạn chọn: Like")
  tokentds = input(vio+"nhập token TDS: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(f) 
    print(xl+"Đăng nhập thành công")
  else:
    print(d+"Nhập sai")
    os.system('clear')
  print(f) 
  write(v+"Tên tài khoản: "+user)
  write(v+"Xu trong tài khoản: "+xu)
  print(f) 
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
    
    idlike=getlike.json()[0]['id']
    urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
    datalike="access_token="+tokenfb
    like=requests.post(urllike, data=datalike)
    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+tokentds).text)
    id=idlike[0:15]
    if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m LIKE >\x1b[1;95m {id} >\x1b[1;93m +300 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
    else:
        print(d+'Lỗi '+id,end='\r')
#tool follow
def tool_follow_function():
  os.system('clear')
  print(banner) 
  print(f) 
  print(v+"Job bạn chọn: Follow")
  tokentds = input(vio+"nhập token TDS: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(xl+"Đăng nhập thành công!! ")
  else:
    print(d+"Lỗi token")
    os.system('clear')
  write(v+"Tên tài khoản: "+user) 
  write(v+"Xu trong tài khoản: "+xu) 
  print(f) 
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getfollow=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds) 
    idfollow=getfollow.json()[0]['id']
    urlfollow='https://graph.facebook.com/'+str(idfollow)+'/likes'
    datafollow="access_token="+tokenfb
    follow=requests.post(urlfollow, data=datafollow)
    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idfollow)+'&access_token='+tokentds).text)
    id=idfollow[0:15]
    if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Follow >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
    else:
        print(d+'Lỗi '+id,end='\r')
#tool reaction
def tool_reaction_function():
  os.system('clear')
  print(banner) 
  write(xl+"Job bạn chọn: Reaction")
  tokentds = input(vio+"nhập token TDS: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(xl+"Đăng nhập thành công!! ")
  else:
    print(d+"Lỗi token")
    os.system('clear')
  write(v+"Tên tài khoản: "+user) 
  write(v+"Xu trong tài khoản: "+xu) 
  print(f) 
  dl=int(input(xb+"Time Delay: "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getreaction=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+tokentds) 
    idreaction=getreaction.json()[0]['id']
    urlreaction='https://graph.facebook.com/'+str(idreaction)+'/reactions'
    datareaction="access_token="+tokenfb
    reaction=requests.post(urlreaction, data=datareaction)
    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LOVE&id='+(idreaction)+'&access_token='+tokentds).text)
    id=idreaction[0:15]
    if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Reaction >\x1b[1;95m {id} >\x1b[1;93m +400 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
    else:
        print(d+'Lỗi '+id,end='\r')
def tool_cmt_function():
  os.system('clear')
  print(banner) 
  write(f) 
  write(xl+"Job bạn chọn: Comment")
  write(f) 
  tokentds = input(vio+"Nhập token tđs: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(f) 
    print(xl+"Đăng nhập thành công")
  else:
    print(d+"Nhập sai")
    os.system('clear')
  print(f) 
  write(v+"Tên tài khoản: "+user)
  write(v+"Xu trong tài khoản: "+xu)
  print(f) 
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getcmt=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+tokentds) 
    idcmt=getcmt.json()[0]['id']
    urlcmt='https://graph.facebook.com/'+str(idcmt)+'/comments'
    datacmt="access_token="+tokenfb
    cmt=requests.post(urlcmt, data=datacmt)
    nhan=json.loads(requests. get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idcmt)+'&access_token='+tokentds).text)
    id=idlike[0:15]
    if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m CMT >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
    else:
        print(d+'Lỗi '+id,end='\r')
menu()