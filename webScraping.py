#!/usr/bin/python3

# @m4lal0

import requests, re, sys, signal, subprocess, time, platform
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from fake_useragent import UserAgent


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def signal_handler(key, frame):
	print(bcolors.DARKCYAN + "\n\n[" + bcolors.YELLOW + "!" + bcolors.DARKCYAN + "]"+ bcolors.RED + " Exiting...\n"+ bcolors.ENDC)
	sys.exit(1)


signal = signal.signal(signal.SIGINT, signal_handler)
user_agent = UserAgent()


def display_banner():
    banner = "\n __       __          __        ______                                      __                   \n"
    banner += "|  \  _  |  \        |  \      /      \                                    |  \                  \n"
    banner += "| ▓▓ / \ | ▓▓ ______ | ▓▓____ |  ▓▓▓▓▓▓\ _______  ______   ______   ______  \▓▓_______   ______  \n"
    banner += "| ▓▓/  ▓\| ▓▓/      \| ▓▓    \| ▓▓___\▓▓/       \/      \ |      \ /      \|  \       \ /      \ \n"
    banner += "| ▓▓  ▓▓▓\ ▓▓  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\\\▓▓    \|  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓\ \▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\\\n"
    banner += "| ▓▓ ▓▓\▓▓\▓▓ ▓▓    ▓▓ ▓▓  | ▓▓_\▓▓▓▓▓▓\ ▓▓     | ▓▓   \▓▓/      ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓\n"
    banner += "| ▓▓▓▓  \▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓__/ ▓▓  \__| ▓▓ ▓▓_____| ▓▓     |  ▓▓▓▓▓▓▓ ▓▓__/ ▓▓ ▓▓ ▓▓  | ▓▓ ▓▓__| ▓▓\n"
    banner += "| ▓▓▓    \▓▓▓\▓▓     \ ▓▓    ▓▓\▓▓    ▓▓\▓▓     \ ▓▓      \▓▓    ▓▓ ▓▓    ▓▓ ▓▓ ▓▓  | ▓▓\▓▓    ▓▓\n"
    banner += " \▓▓      \▓▓ \▓▓▓▓▓▓▓\▓▓▓▓▓▓▓  \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓       \▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ \▓▓\▓▓   \▓▓_\▓▓▓▓▓▓▓\n"
    banner += "                                                                  | ▓▓                 |  \__| ▓▓\n"
    banner += "                                                                  | ▓▓                  \▓▓    ▓▓\n"
    banner += "                                                                   \▓▓                   \▓▓▓▓▓▓ \n"
    return print(bcolors.YELLOW + banner + bcolors.ENDC)


def scrapeando():
    print(bcolors.BOLD + "\t\t\t\tWEBSCRAPING PARA NO PROGRAMADORES\n" + bcolors.ENDC)
    print(bcolors.BLUE + "Descripción:" + bcolors.ENDC + bcolors.DARKCYAN + "\n\tEn esta sección podras realizar webscraping colocando el selector de lo que requieres de un sitio web" + bcolors.ENDC)
    print(bcolors.BLUE + "\nEjemplo:" + bcolors.ENDC)
    print(bcolors.RED + "\tURL de prueba:" + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\t\thttps://www.tabascohoy.com/" + bcolors.ENDC)
    print(bcolors.RED + "\tSelector de prueba:" + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\t\t#zox_flex_list1_widget-3 > div > div.zox-widget-flex1-adl > div > div > section.zox-art-wrap.zoxrel.zox-art-main > div > div.zox-art-text > div > div.zox-art-title > a > h2" + bcolors.ENDC + "\n\n-----")
    url = input(bcolors.DARKCYAN + "\n\n[" + bcolors.YELLOW +"?" + bcolors.DARKCYAN +"]" + bcolors.YELLOW + " URL: " + bcolors.ENDC)
    selector = input(bcolors.DARKCYAN + "[" + bcolors.YELLOW +"?" + bcolors.DARKCYAN +"]" + bcolors.YELLOW + " Selector: " + bcolors.ENDC)

    print(bcolors.BOLD + "\nScrapeando la url:" + bcolors.ENDC)
    print(bcolors.BLUE + url + bcolors.ENDC)
    print(bcolors.BOLD + "\nBuscando el selector:" + bcolors.ENDC)
    print(bcolors.GREEN + selector + bcolors.ENDC)

    # Reemplazo nth-child por nth-of-type.
    selector = selector.replace("nth-child", "nth-of-type")

    response = requests.get(url)

    bs = BeautifulSoup(response.text, "html.parser")

    elements = bs.select(selector)

    found = False
    count = 1
    for element in elements:
        print(bcolors.BOLD + "\nResultado número: " + str(count) + bcolors.ENDC)
        print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)
        print(element.text)
        print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)
        found = True
        count += 1

    if not found:
        print(bcolors.DARKCYAN + "\n\n[" + bcolors.RED + "X" + bcolors.DARKCYAN + "]"+ bcolors.RED + " No se encontraron resultados...\n"+ bcolors.ENDC)


def youtube():
    print(bcolors.BOLD + "\t\t\tDESCARGA SUBTITULOS DE UN VIDEO DE YOUTUBE\n" + bcolors.ENDC)
    print(bcolors.BLUE + "Descripción:" + bcolors.ENDC + bcolors.DARKCYAN + "\n\tEn esta sección podras descargar los subtitulos de un video de Youtube." + bcolors.ENDC + "\n\n-----")
    video_id=input(bcolors.DARKCYAN + "\n\n[" + bcolors.YELLOW +"?" + bcolors.DARKCYAN +"]" + bcolors.YELLOW + " ID del Video: " + bcolors.ENDC)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])

    print(bcolors.BOLD + "\nResultado de subtitulos: " + bcolors.ENDC)
    print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)
    for transcript in transcript_list:
        print(transcript)
    
    print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)


def get_contacts(name: str):
    contacts = []
    base_url = "https://www.seccionamarilla.com.mx/resultados/%s/"

    headers = {
        'User-Agent': user_agent.random
    }
    url = base_url % name + "1/"
    response = requests.get(url, headers=headers)
    bs = BeautifulSoup(response.text, "html.parser")

    ul = bs.find("ul", class_="list")
    lis = ul.find_all("li")
    for li in lis:
        # Name
        div_name = li.find("div", class_="row l-info")
        div2_name = div_name.find("div", class_="six columns l-datos")
        a_name = div2_name.find("a")
        h2_name = a_name.find("h2")
        span_name = h2_name.find("span")
        name = span_name.string

        # Address
        div_address = li.find("div", class_="row l-info")
        div2_address = div_address.find("div", class_="six columns l-datos")
        div3_address = div2_address.find("div", class_="l-address")
        spans_address = div3_address.find_all("span")
        street_address = spans_address[0].string.strip()
        street_address = re.sub(' +', ' ', street_address)
        locality_address = spans_address[1].string.strip()
        region_address = spans_address[2].string.strip()

        # Phone number
        div_number = li.find("div", class_="row l-info")
        div2_number = div_number.find("div", class_="six columns l-datos")
        div_phone = div2_number.find("div", class_="l-tel")
        span_number = div_phone.find("span", itemprop="telephone")
        phone_number = span_number.string

        dict_contact = {
            'name': name,
            'phone_number': phone_number,
            'address': {
                'street' : street_address,
                'locality' : locality_address,
                'region' : region_address
            }
        }

        contacts.append(dict_contact)

    return contacts


def search_contacts():
    print(bcolors.BOLD + "\t\t\t\tBUSQUEDA EN LA SECCION AMARILLA MX\n" + bcolors.ENDC)
    print(bcolors.BLUE + "Descripción:" + bcolors.ENDC + bcolors.DARKCYAN + "\n\tEn esta sección podra buscar personas/empresas y le desplegará la información de contacto." + bcolors.ENDC + "\n\n-----")
    name = input(bcolors.DARKCYAN + "\n\n[" + bcolors.YELLOW +"?" + bcolors.DARKCYAN +"]" + bcolors.YELLOW + " Empresa o Persona a buscar: " + bcolors.ENDC)
    name = name.replace(' ', '-')
    contacts = get_contacts(name)
    print(bcolors.BOLD + "\nResultados: " + bcolors.ENDC)
    print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)
    for contact in contacts:
        address = contact['address']['street'] + ' ' + contact['address']['locality'] + ' ' + contact['address']['region']
        contact_str = "\n%s \n\t%s \n\t%s" % (contact['name'], address, contact['phone_number'])
        print(contact_str)
    print(bcolors.YELLOW + "=======================================================================" + bcolors.ENDC)


def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(0.1)


def main():
    clear()
    display_banner()
    print("\n\t\t\t     " + bcolors.YELLOW + "[" + bcolors.ENDC + bcolors.BOLD + " M E N U " + bcolors.ENDC + bcolors.YELLOW + "]" + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\n\t\t[" + bcolors.YELLOW +"1" + bcolors.DARKCYAN +"]" + bcolors.PURPLE + " Scrapeando sitio web de manera manual." + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\t\t[" + bcolors.YELLOW +"2" + bcolors.DARKCYAN +"]" + bcolors.PURPLE + " Descargar subtitulos de un video de Youtube." + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\t\t[" + bcolors.YELLOW +"3" + bcolors.DARKCYAN +"]" + bcolors.PURPLE + " Buscar en Sección Amarilla MX." + bcolors.ENDC)
    print(bcolors.DARKCYAN + "\t\t[" + bcolors.YELLOW +"0" + bcolors.DARKCYAN +"]" + bcolors.PURPLE + " Exit." + bcolors.ENDC)

    menu_option = input(bcolors.BOLD + "\n\tChoose option: " + bcolors.ENDC)

    if menu_option == "1":
        clear()
        display_banner()
        scrapeando()
    elif menu_option == "2":
        clear()
        display_banner()
        youtube()
    elif menu_option == "3":
        clear()
        display_banner()
        search_contacts()
    elif menu_option == "0":
        print(bcolors.DARKCYAN + "\n[" + bcolors.YELLOW + "!" + bcolors.DARKCYAN + "] "+ bcolors.RED + "Exiting...\n"+ bcolors.ENDC)
        sys.exit(0)
    else:
       print(bcolors.DARKCYAN + "\n[" + bcolors.RED + "X" + bcolors.DARKCYAN + "] "+ bcolors.RED + "Invalid Option...\n"+ bcolors.ENDC)
       time.sleep(1)
       main()


if __name__ == '__main__':
    main()