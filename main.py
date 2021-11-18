import socket
import ssl
import Geheimnisse
from dataclasses import dataclass
from datetime import datetime
import urllib.request
import threading
import simpleobsws
import asyncio
from playsound import playsound

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='1234', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request(scene):
    await ws.connect() # Make the connection to OBS-Websocket
    #result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    #await asyncio.sleep(1)
    data = {'scene-name':scene}
    result = await ws.call('SetCurrentScene', data) # Make a request with the given data
    print(result)
    await ws.disconnect() # Clean things up by disconnecting. Only really required in a few specific situations, but good practice if you are done making requests or listening to events.

async def on_switchscenes(data):
    print('Scene switched to "{}". It has these sources: {}'.format(data['scene-name'], data['sources']))

bot_username = 'brutzie'
channel_name = 'thebrutzler'
# GeheimSchluessel = 'kjslkdjflsdjföljsdölf213173'
oauth_token = Geheimnisse.GeheimSchluessel
html_original = 'http://192.168.1.175/win&A=128&CL=hFFF6F7&C2=h0000FF&FX=9&SX=128&IX=128&FP=0'
html_original_2 = 'http://192.168.1.140/win&A=128&CL=hFFF6F7&C2=h0000FF&FX=9&SX=128&IX=128&FP=0'

timer_sound = 1


def ursprungszustand():
    urllib.request.urlopen(html_original)
    urllib.request.urlopen(html_original_2)
    urllib.request.urlcleanup()
    print('5 Sekunden Später')
    
#T = threading.Timer (5,ursprungszustand)

@dataclass
class TwitchMessage:
    User: str
    Message: str
    Host: str
    Channel: str
    Type: str



# Beispielhafte Funktion, um auf ein Kommando zu reagieren
def print_dicsord(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Discord: https://discord.gg/gstWkyK (Kurzschluss Junkies)'
    send_chat(irc, output, channel_name)
    
# Beispielhafte Funktion, um auf ein Kommando zu reagieren
def print_eieiei(msg: TwitchMessage):
    output = f'Hey @{msg.User}, EiEiEi Anleitung: https://kurzschluss-blog.de/eieiei-give-away-ostern-2021-aufbauanleitung/' 
    send_chat(irc, output, channel_name)

# Beispielhafte Funktion, um auf ein Kommando zu reagieren
def print_eckeckeck(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Sammelpool: https://www.paypal.com/pools/c/8yvqaYVlNZ' 
    send_chat(irc, output, channel_name)

# Funktion zum Ausgeben der einzelnen Kommandos, die in em Dictionary stehen
def print_commands(msg: TwitchMessage):
    is_first = True
    output = f'Hey @{msg.User} - Kommandosliste: '
    for cmd in cmd_dictionary:
        if is_first:
            output += cmd
            is_first = False
        else:
            output += f', {cmd}'
    send_chat(irc, output, channel_name)

def print_toollist(msg: TwitchMessage):
    is_first = True
    output = f'Hey @{msg.User} - Werkzeugliste: '
    for cmd in tool_dictionary:
        if is_first:
            output += cmd
            is_first = False
        else:
            output += f', {cmd}'
    send_chat(irc, output, channel_name)
    
def print_software(msg: TwitchMessage):
    is_first = True
    output = f'Hey @{msg.User} - Softwareliste: '
    for cmd in software_dictionary:
        if is_first:
            output += cmd
            is_first = False
        else:
            output += f', {cmd}'
    send_chat(irc, output, channel_name)
    
def print_sound(msg: TwitchMessage):
    is_first = True
    output = f'Hey @{msg.User} - Soundliste: '
    for cmd in sound_dictionary:
        if is_first:
            output += cmd
            is_first = False
        else:
            output += f', {cmd}'
    send_chat(irc, output, channel_name)

def print_podcast(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Was auf die Ohren: https://open.spotify.com/show/0cVhOe5kMlmPpYw7XmRFuK'
    send_chat(irc, output, channel_name)   
    
def print_lupe(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Lupe: Kein Plan. Will sowieso Eine neue'
    send_chat(irc, output, channel_name)
    
def print_spielgeld(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Unterstützung: https://www.paypal.com/pools/c/8ytzVbK1Gz'
    send_chat(irc, output, channel_name)

def print_spende(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Unterstützung: https://streamlabs.com/thebrutzler/tip'
    send_chat(irc, output, channel_name)

def print_ESP31(msg: TwitchMessage):
    output = f'Hey @{msg.User}, der ESP31 link: https://github.com/theBrutzler/ESP31'
    send_chat(irc, output, channel_name)
    
def print_BLE(msg: TwitchMessage):
    output = f'Hey @{msg.User}, der BLE_Keyboard link: https://github.com/theBrutzler/BLE_Keyboard'
    send_chat(irc, output, channel_name)

def print_homepage(msg: TwitchMessage):
    output = f'Hey @{msg.User}, theBrutzler\'s Page: http://thebrutzler.de'
    send_chat(irc, output, channel_name)   

def print_tischcam(msg: TwitchMessage):
    output = f'Hey @{msg.User}, TischCam: https://www.amazon.de/gp/product/B08FR6M1ZV'
    send_chat(irc, output, channel_name)

def print_facecam(msg: TwitchMessage):
    output = f'Hey @{msg.User}, FaceCam: https://www.amazon.de/gp/product/B0002HAHUY'
    send_chat(irc, output, channel_name)
    
def print_matte(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Lötmatte: https://www.amazon.de/Preciva-Silikonmatte-Hitzebest%C3%A4ndige-Arbeitsmatte-Arbeitsunterlage/dp/B075D9R8PZ/'
    send_chat(irc, output, channel_name)
    
def print_kolben1(msg: TwitchMessage):
    output = f'Hey @{msg.User}, FeinKolben: https://de.aliexpress.com/item/1005001961352680.html'
    send_chat(irc, output, channel_name)
    
def print_kolben2(msg: TwitchMessage):
    output = f'Hey @{msg.User}, DualKolben: https://de.aliexpress.com/item/4001363914362.html'
    send_chat(irc, output, channel_name)

def print_kicad(msg: TwitchMessage):
    output = f'Hey @{msg.User}, KiCad: https://kicad.org/download'
    send_chat(irc, output, channel_name)

def print_freecad(msg: TwitchMessage):
    output = f'Hey @{msg.User}, FreeCad: https://www.freecadweb.org/downloads.php'
    send_chat(irc, output, channel_name)
    
def print_paint(msg: TwitchMessage):
    output = f'Hey @{msg.User}, WindowsPaint: https://www.chip.de/downloads/c1_downloads_auswahl_105843239.html'
    send_chat(irc, output, channel_name)
    
def print_notepad(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Notepad++: https://notepad-plus-plus.org/downloads'
    send_chat(irc, output, channel_name)

def print_forum(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Forum: https://kurzschluss-junkies.de'
    send_chat(irc, output, channel_name)

def print_github(msg: TwitchMessage):
    output = f'Hey @{msg.User}, GIT: https://github.com/theBrutzler https://desktop.github.com'
    send_chat(irc, output, channel_name)

def print_navi(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Navilink: https://www.paypal.com/pools/c/8AcwoUWtGh'
    send_chat(irc, output, channel_name)

def print_mikroskop(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Mikroskop: https://vevor.de/products/simul-fokale-trinokular-stereo-3-5x-90x-zoom-mikroskop-stereomikrosko'
    send_chat(irc, output, channel_name)

def print_hack(msg: TwitchMessage):
    output = f'Hey @{msg.User}, Das ist der Hackaday link: https://hackaday.io/project/179890-india-navi lass gerne ein like da :)'
    send_chat(irc, output, channel_name)

def sound_nice(msg: TwitchMessage):
    playsound('nice.mp3')

def sound_laugh(msg: TwitchMessage):
    playsound('laughing.mp3')
    
def sound_haha(msg: TwitchMessage):
    playsound('haha.mp3')
    
def sound_hey(msg: TwitchMessage):
    playsound('hey.mp3')

def sound_wait(msg: TwitchMessage):
    playsound('Think_Music.wav')

def sound_anwalt(msg: TwitchMessage):
    playsound('anwalt.mp3')
 
def sound_skoll(msg: TwitchMessage):
    playsound('skoll.wav') 

def sound_saber(msg: TwitchMessage):
    playsound('saber.mp3')
    
def handle_command(message: TwitchMessage):
    # erstes Wort extrahieren
    first_word = message.Message.split(' ', 1)[0]
    
    # testen, ob irgendein Kommando mit diesem ersten Wort beginnt
    cmd_dict = {}
    cmd_dict.update(cmd_dictionary)
    cmd_dict.update(tool_dictionary)
    cmd_dict.update(software_dictionary)
    global timer_sound
    global sound_timer_timeout
    if timer_sound == True:
        timer_sound = False
        cmd_dict.update(sound_dictionary)
        sound_timer = threading.Timer (sound_timer_timeout,reset_sound_timer)
        sound_timer.start()
    for key in cmd_dict:
        if key in first_word:
            cmd_dict[key](message)
        elif first_word.startswith('!'):
            print('unknown cmd')
    if (message.User == "streamlabs" or message.User == "soundalerts")  and ( "for following" in message.Message or "has cheered" in message.Message or "just"  in message.Message or "played"  in message.Message):
    #if message.User == "thebrutzler" and ( "for following" in message.Message or "has cheered" in message.Message or "just"  in message.Message ):
        with urllib.request.urlopen('http://192.168.1.175/url') as response:
           html = response.read()
        html_split = html.decode().split("\"", 2)
        #html_original = html_split[1]
        print (html_split[1])
        urllib.request.urlopen('http://192.168.1.175/win&A=128&CL=hFF00FF&C2=h0000FF&FX=90&SX=128&IX=255&FP=4')
        urllib.request.urlopen('http://192.168.1.140/win&A=128&CL=hFF00FF&C2=h0000FF&FX=90&SX=128&IX=255&FP=4')
        urllib.request.urlcleanup()
        print('Follow oder so')
        print(message.User)
        T = threading.Timer (10,ursprungszustand)
        T.start()
    if "@thebrutzler" in message.Message:
        playsound('icq.wav')
    if message.User == "melli1083":
        playsound('rooobert.mp3')


    if message.User == "thebrutzler" and "!lötplatz" in message.Message:
        loop.run_until_complete(make_request('Lötplatz'))
        
    if message.User == "thebrutzler" and "!desktop" in message.Message:
        loop.run_until_complete(make_request('Ready'))
        
    if message.User == "thebrutzler" and "!maincam" in message.Message:
        loop.run_until_complete(make_request('Facecam'))

    if message.User == "thebrutzler" and "!mikro" in message.Message:
        loop.run_until_complete(make_request('Mikroskop'))

    if message.User == "brutzie" and "!ladybug" in message.Message:
        playsound('ladybug.wav')


    timeout = 60 
    global timer_diekleinehexemoni
    if message.User == "diekleinehexemoni" and timer_diekleinehexemoni == True:
        playsound('diekleinehexemoni_sound.wav')
        print('diekleinehexemoni_sound.wav')
        timer_diekleinehexemoni = False
        diekleinehexemoni = threading.Timer (timeout, reset_timer_diekleinehexemoni)
        diekleinehexemoni.start()

        
# hier sind alle Kommandos mit Funktionsaufrufen gespeichert
# die Funktionen muessen weiter oben stehen, sonst werden sie als not defined gewertet
cmd_dictionary = {
    '!command': print_commands,
    '!bot': print_commands,
    '!hilfe': print_commands,
    '!help': print_commands,
    '!discord': print_dicsord, 
    '!eieiei': print_eieiei,
    '!spielgeld': print_spielgeld,
    '!spende': print_spende,
    '!tool': print_toollist,
    '!werkzeug': print_toollist,
    '!software': print_software,
    '!podcast': print_podcast,
    '!eck': print_eckeckeck,
    '!homepage': print_homepage,
    '!sound': print_sound,
    '!forum': print_forum,
    '!git': print_github,
    '!navi': print_navi,
    '!hack': print_hack
    
}
tool_dictionary = {
    '!lupe': print_lupe,
    '!tischcam': print_tischcam, 
    '!facecam': print_facecam, 
    '!kolben1': print_kolben1,
    '!kolben2': print_kolben2,
    '!matte': print_matte,
    '!mikroskop': print_mikroskop
}
software_dictionary = {
    '!schaltplan': print_kicad,
    '!cad': print_freecad,
    '!layout': print_kicad,
    '!kicad': print_kicad,
    '!malen': print_paint, 
    '!programmieren': print_notepad,
    '!esp31': print_ESP31,
    '!ble': print_BLE
}

sound_dictionary = {
    '!nice': sound_nice,
    '!laugh': sound_laugh,
    '!haha': sound_haha,
    '!hey': sound_hey,
    '!wait': sound_wait,
    '!anwalt': sound_anwalt,
    '!saber': sound_saber,
    '!skål': sound_skoll
}



steamlaps_dictonary = {
    
    }

# Nachricht in den IRC senden
def send(m_irc: ssl.SSLSocket, message: str):
    m_irc.send(bytes(f'{message}\r\n', 'UTF-8'))


# Chatmessage fuer Twitch-Chat vorbereiten
def send_chat(m_irc: ssl.SSLSocket, message: str, channel: str):
    send(m_irc, f'PRIVMSG #{channel} :{message}')


# alle 5 Minuten wird das hier getriggert - Antwort auf 'ping'
def send_pong(m_irc: ssl.SSLSocket):
    print(f'sending pong ({datetime.now()})')
    send(m_irc, 'PONG :tmi.twitch.tv')

# Message auseinandernehmen
def extract_message(raw_message: str) -> TwitchMessage:
    components = raw_message.split()
    user, host = components[0].split('!')[1].split('@')
    m_type = components[1]
    channel = components[2]
    message = ' '.join(components[3:])[1:]
    retval = TwitchMessage(User=user, Message=message, Host=host, Type=m_type, Channel=channel)
    return retval


# Einstiegspunkt
if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    irc = context.wrap_socket(socket)

    irc.connect(('irc.chat.twitch.tv', 6697))

    print(f'connected to {channel_name} - sending credentials for {bot_username}')

    send(irc, f'PASS oauth:{oauth_token}')
    send(irc, f'NICK {bot_username}')
    send(irc, f'JOIN #{channel_name}')

    connected = False

    while True:
        data = irc.recv(4096)
        raw_message = data.decode('UTF-8')

        try:
            for line in raw_message.split('\r\n'):
                if line.strip() == '':
                    pass
                elif line.startswith('PING :tmi.twitch.tv'):
                    send_pong(irc)
                elif line.startswith(':tmi.twitch'):
                    print(line)
                elif line.startswith(f':{bot_username}'):
                    print(line)
                    if not connected:
                        print(f'authorized ({datetime.now()})')
                        connected = True
                elif line.startswith(':'):
                    message_obj = extract_message(line)
                    handle_command(message_obj)
                else:
                    print(f'undetectable - {line}')
        except Exception as ex:
            print('--- Exception ---')
            print(type(ex))
            print(ex.args)
            print('--- Exception End ---')
