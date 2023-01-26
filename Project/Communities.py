import os


def get_word_from_list(parts : list[str], connector : chr = " "):
    new_word = ""
    for i in range(len(parts)-1):
        new_word = new_word + parts[i] + connector
    return new_word + parts[len(parts)-1]


def get_name_and_type(chain : str):
    refactor_needed = False
    val = chain.strip().split(" ")
    type = None
    if len(val) > 1:
        refactor_needed = True
    if refactor_needed:
        starting_index = 0
        if val[0][0] == 'm' or val[0][0] == 'g':
            starting_index = 1
            if len(val[0]) == 2:
                type = 'miasto'
            elif len(val[0]) == 5:
                type = 'wies'
            else:
                type = 'gmina miejsko-wiejska'
        else:
            type = 'miasto'
        name = get_word_from_list(val[starting_index:])
    else:
        name = val[0]
        type = 'miasto'
    return name, type


def create_clear_data():
    file_names = os.listdir('Original_data/Communities')
    for i in file_names:
        # first import data from all .csv
        original_data_path = f"Original_data/Communities/{i}"
        clear_data_path = f"Clear_data/Communities/{i}"
        voyvodship = i.replace("\n", "").replace(".csv", "").strip()
        original_data_list = [[], [], []]
        with open(original_data_path, encoding='utf-8-sig') as file:
            for line in file:
                line_data = line.split(";")
                for j in range(3):
                    original_data_list[j].append(line_data[j])
        # then convert it to desired format
        clear_data_list = [[], [], [], [], [], []]
        county = None
        for j in range(len(original_data_list[0])):
            first_col = original_data_list[0][j].strip()
            if first_col[:3] == 'WOJ' or first_col[:5] == 'Miast' or first_col[:3] == 'Cit':
                county = None
            elif first_col[:6] == 'Powiat':
                fc_list = first_col.split(" ")
                county = get_word_from_list(fc_list[1:])
            else:
                name, type = get_name_and_type(original_data_list[0][j])
                id = int(original_data_list[1][j])
                citizens = int(original_data_list[2][j])
                clear_data_list[0].append(id)
                clear_data_list[1].append(name)
                clear_data_list[2].append(type)
                clear_data_list[3].append(citizens)
                clear_data_list[4].append(voyvodship)
                if county is not None:
                    clear_data_list[5].append(county)
                else:
                    clear_data_list[5].append(name)
        # write it to all .csv
        with open(clear_data_path, "w", encoding='utf8') as file:
            for j in range(len(clear_data_list[0])):
                for k in range(len(clear_data_list)-1):
                    file.write(f"{clear_data_list[k][j]};")
                file.write(f"{clear_data_list[len(clear_data_list)-1][j]}\n")
        # for c in clear_data_list:  # - uncomment if want to see debugging print
        #     print(c)
    # finally write it to one big .csv
    if os.path.exists("Clear_data/Communities/all_data.csv"):
        os.remove("Clear_data/Communities/all_data.csv")
    file_names = os.listdir('Clear_data/Communities')
    with open("Clear_data/Communities/all_data.csv", "w", encoding='utf8') as w_file:
        w_file.write("id;nazwa;typ;liczba_mieszkancow;wojewodztwo;powiat\n")
        for i in file_names:
            clear_data_path = f"Clear_data/Communities/{i}"
            with open(clear_data_path, encoding='utf8') as r_file:
                for line in r_file:
                    w_file.write(line)
