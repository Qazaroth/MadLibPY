import json, random

data_file = open("data.json", "r")
data_raw = data_file.read()

data_json = json.loads(data_raw)

templates = data_json["templates"]
templates_length = len(templates)

if templates_length > 0:
    random_number = random.randint(0, templates_length - 1)
    random_template = templates[random_number]
    
    template_title = random_template["title"]
    template_blanks = random_template["blanks"]
    template_value = random_template["value"][:-1]

    while len(template_blanks) > 2:
        random_number = random.randint(0, templates_length - 1)
        random_template = templates[random_number]
        
        template_title = random_template["title"]
        template_blanks = random_template["blanks"]
    
    list_blanks = template_blanks
    blanks_input_list = []

    for blank in list_blanks:
        blank_input = input("{}: ".format(blank))

        blanks_input_list.append(blank_input)

    print(blanks_input_list)
    # print("Title: {}\nBlanks [{}]\nValue: {}".format(template_title, template_blanks, template_value))
        