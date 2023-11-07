import os

# Define the base folder where you want to create the files
base_folder = 'C:/Data/SK.Data/abacus/abacus/'  # Replace with the actual path

head_template = "C:/Data/SK.Data/abacus/abacus/common/head_template.html"
body_template = "C:/Data/SK.Data/abacus/abacus/common/body_template.html"
footer_template = "C:/Data/SK.Data/abacus/abacus/common/foot_template.html"

link_file = "links.txt"
links = ["Level Folder \t\t\t\t:\t\t\t\t URL Link"]
links.append("\n")
github_path = "https://base2ace.github.io/abacus/"
banner_file_path = r'C:/Data/SK.Data/abacus/abacus/common/banner.html'
footer_file_path = r'C:/Data/SK.Data/abacus/abacus/common/footer.html'

def update_sheet_content(folder_path, filename, head, foot):
    # Open the sheet in read mode and read the content.
    existing_content = ""
    with open(os.path.join(folder_path, filename), 'r') as html_file:
        existing_content =  html_file.readlines()

        existing_body = ""
        for line in existing_content:
            if "section" in line:
                existing_body += line

    # Open the file in wite mode and modify it.
    with open(os.path.join(folder_path, filename), 'w') as html_file:
        content = head + existing_body + foot
        html_file.write(content)

def create_file(folder_path, filename, content = "", full_link_path = "", sheet_folder = ""):
    with open(os.path.join(folder_path, filename), 'w') as html_file:
        html_file.write(content)
        if full_link_path != "":
            links.append(sheet_folder + "\t:\t" + full_link_path + "/" + filename)

def create_link_file(folder_path, link_file, content = ""):
    with open(os.path.join(folder_path, link_file), 'w') as link_file:
        link_file.write(content)

# Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Iterate through the lines and process each path
for line in lines:
    path = line.strip()
    parts = path.split('/')
    filename = 'sheet.html'
    remainder_path = '/'.join(parts)
    full_link_path = github_path + remainder_path
    folder_path = os.path.join(base_folder, '/'.join(parts))
    content = ""
    head = ""
    body = ""
    foot = ""

    # Create the folder hierarchy
    os.makedirs(folder_path, exist_ok=True)

    current_directory = folder_path
    banner_relative_path = os.path.relpath(banner_file_path, current_directory)
    footer_relative_path = os.path.relpath(footer_file_path, current_directory)

    # add head
    with open(head_template, "r") as head:
        head = head.read()

    head = head.replace("Heading", parts[-1])
    banner_rel_path_str = 'src="' + banner_relative_path + '"'
    head = head.replace('src="../../../common/banner.html"', banner_rel_path_str)

    # # add body only the first time .. skip the body as it may have been modified as new sections are added.
    # with open(body_template, "r") as body:
    #     body = body.read()

    # add footer
    with open(footer_template, "r") as foot:
        foot = foot.read()
        footer_rel_path_str = 'src="' + footer_relative_path + '"'
        foot = foot.replace('src="../../../common/footer.html"', footer_rel_path_str)


    content = head + body + foot


    # Create empty HTML files within the base folder
    # create_file(folder_path, "section1.html")
    # create_file(folder_path, "section2.html")
    # create_file(folder_path, "section3.html")
    # create_file(folder_path, "section4.html")

    # Create and write the HTML file within the base folder. This has to be done once only.
    # create_file(folder_path, filename, content, full_link_path, remainder_path)

    update_sheet_content(folder_path, filename, head, foot)

create_link_file(base_folder, link_file, "\n".join(links))

print("HTML files have been created.")
