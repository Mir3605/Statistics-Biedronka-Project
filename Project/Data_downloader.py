import os.path
from Communities import get_word_from_list
import urllib.request
import urllib.error
import urllib.parse
import sqlite3


def convert_char(c : chr):
    utf8_letters = ['ą', 'ę', 'ć', 'ż', 'ź', 'ó', 'ł', 'ń', 'ś', 'Ć', 'Ż', 'Ź', 'Ó', 'Ł', 'Ś']
    ascii_letters = ['a', 'e', 'c', 'z', 'z', 'o', 'l', 'n', 's', 'C', 'Z', 'Z', 'O', 'L', 'S']
    for i in range(len(utf8_letters)):
        if utf8_letters[i] == c:
            return ascii_letters[i]
    return c


def convert_word(word : str):
    new_word = ""
    for i in range(len(word)):
        new_word = new_word + convert_char(word[i])
    return new_word.lower().replace(" ", "-")


def get_voyvodhip_postcode(voyvodship : str):
    postcodes = {'Mazowieckie':0, 'Warmińsko-mazurskie':1, 'Podlaskie':1, 'Lubelskie':2, 'Świętokrzyskie':2,
                 'Małopolskie':3, 'Podkarpackie':3, 'Śląskie':4, 'Opolskie':4, 'Dolnośląskie':5, 'Wielkopolskie':6,
                 'Lubuskie':6, 'Zachodniopomorskie':7, 'Pomorskie':8, 'Kujawsko-pomorskie':8, 'Łódzkie':9}
    if voyvodship in postcodes.keys():
        return postcodes.get(voyvodship)
    return None


def create_url(city : str, page_no : int):
    return f"https://www.biedronka.pl/pl/sklepy/lista,city,{convert_word(city)},page,{page_no}"


def get_postcode(line : str):
    return line.strip(" ").replace('<br />', '').replace('\n', '')


def get_street(line : str):
    return line.replace('</span>', '').replace('\n', '').strip()


def get_opening_hours(line : str):
    current_opening_hours = line.replace('</span><br />', '').replace('\n', '')
    if current_opening_hours[len(current_opening_hours)-1] == 'e':
        return 'Zamknięte'
    return current_opening_hours[-11:]


def read_and_save(community_id, shop_id : int, previous_page_first_address : str = None):
    lines_counter = 0
    next_is_shop_address = 0
    next_are_opening_hours = 0
    postcodes = []
    addresses = []
    opening_hours = [[] for _ in range(7)]
    need_to_check_next = True
    with open("temp_data.html") as f:
        for line in f:
            if line == '\n':
                pass
            elif line == '		        <ul class="shopList">\n':
                lines_counter = 499
            elif lines_counter > 1:
                lines_counter -= 1
                if line == '		<div class="pagination">\n':
                    lines_counter = 0
                    break
                elif line == '<section class="newShopSearch">':
                    lines_counter = 0
                    need_to_check_next = False
                    break
                elif next_is_shop_address == 1:
                    street = get_street(line)
                    if street == previous_page_first_address:
                        return shop_id, False, previous_page_first_address
                    addresses.append(street)
                    next_is_shop_address = 0
                elif next_is_shop_address == 2:
                    next_is_shop_address = 1
                    postcode = get_postcode(line)
                    postcodes.append(postcode)
                elif line == '                    <span class="shopAddress">\n':
                    next_is_shop_address = 2
                elif next_are_opening_hours > 0:
                    opening_hours[7 - next_are_opening_hours].append(get_opening_hours(line))
                    next_are_opening_hours -= 1
                elif line == '                        <b>Godziny otwarcia:</b><br />\n':
                    next_are_opening_hours = 7
            if lines_counter == 1:
                break
    if len(addresses) == 0:
        return shop_id, False, previous_page_first_address
    all_shops_path = 'Clear_data/Shops/all_shops.csv'
    if not os.path.exists(all_shops_path):
        with open(all_shops_path, 'w', encoding='utf8') as f:
            f.write('id_gminy;id_sklepu;kod_pocztowy;ulica\n')
    opening_hours_path = 'Clear_data/Shops/all_opening_hours.csv'
    if not os.path.exists(opening_hours_path):
        with open(opening_hours_path, 'w', encoding='utf8') as f:
            f.write('id_sklepu;poniedzialek;wtorek;sroda;czwartek;piatek;sobota;niedziela\n')
    with open(all_shops_path, 'a', encoding='utf8') as as_file:
        with open(opening_hours_path, 'a', encoding='utf8') as oh_file:
            for i in range(len(postcodes)):
                as_file.write(f'{community_id};{shop_id};{postcodes[i]};{addresses[i]}\n')
                oh_list = [opening_hours[j][i] for j in range(7)]
                oh_string = get_word_from_list(oh_list, ';')
                oh_file.write(f'{shop_id};{oh_string}\n')
                shop_id += 1
    return shop_id, need_to_check_next, addresses[0]


if __name__ == '__main__':
    db = sqlite3.connect('Database/shops.db')
    cursor = db.cursor()
    cursor.execute('''
    SELECT id, nazwa, wojewodztwo FROM gminy ORDER BY nazwa, liczba_mieszkancow DESC
    ''')
    rows = cursor.fetchall()
    db.close()
    shop_id = 1
    all_shops_path = 'Clear_data/Shops/all_shops.csv'
    if os.path.exists(all_shops_path):
        os.rename(all_shops_path, 'Clear_data/Shops/all_shops_old.csv')
    with open(all_shops_path, 'w', encoding='utf8') as f:
        f.write('id_gminy;id_sklepu;kod_pocztowy;ulica\n')
    opening_hours_path = 'Clear_data/Shops/all_opening_hours.csv'
    if os.path.exists(opening_hours_path):
        os.rename(opening_hours_path, 'Clear_data/Shops/all_opening_hours_old.csv')
    with open(opening_hours_path, 'w', encoding='utf8') as f:
        f.write('id_sklepu;poniedzialek;wtorek;sroda;czwartek;piatek;sobota;niedziela\n')
    prev_name = None
    for r in rows:
        id = r[0]
        name = r[1]
        if name != prev_name:
            prev_name = name
            voyvodship = r[2]
            page_no = 1
            need_to_check_next = True
            first_address = None
            while need_to_check_next:
                url = create_url(name, page_no)
                print(f'Checking another url {url}')
                response = urllib.request.urlopen(url)
                web_data = response.read().decode('UTF-8')
                with open('temp_data.html', 'w') as file:
                    file.write(web_data)
                shop_id, need_to_check_next, first_address = read_and_save(id, shop_id, first_address)
                page_no += 1

    print('finished :)')


