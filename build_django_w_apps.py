import os

'''
FYI: This script will only generate project's within the same
directory as its self.
'''


def clear():
    os.system('cls' if os.name == "nt" else 'clear')


def build_filesys():
    os.system("say 'Building {} Project'".format(APP_NAME))

    os.system("django-admin startproject {}_main".format(PROJ_NAME))
    os.rename(PROJ_NAME+"_main", PROJ_NAME+"_proj")
    os.chdir('{}_proj'.format(PROJ_NAME))
    root_dir = os.getcwd()
    os.mkdir("apps")

    os.chdir("apps")
    os.system("touch __init__.py")
    os.system("python ../manage.py startapp {}".format(APP_NAME))

    os.chdir(APP_NAME)
    os.system("touch urls.py")
    os.makedirs("templates/{}".format(APP_NAME))

    os.mkdir("static")
    os.chdir("static")
    os.makedirs("{}/css".format(APP_NAME))
    os.chdir("{}".format(APP_NAME))
    os.makedirs("img".format(APP_NAME))
    os.makedirs("js".format(APP_NAME))
    os.chdir("../../")

    os.chdir("templates/{}".format(APP_NAME))
    os.system("touch index.html")
    os.chdir("../../static/{}/css".format(APP_NAME))
    os.system("touch style.css")
    return root_dir


def build_history(root_dir):
    seen_dir = []
    seen_files = []
    for root, dirs, files in os.walk(root_dir):
        for directory in dirs:
            seen_dir.append(directory)
        for file in files:
            seen_files.append(file)

    print("\nCREATED THE FOLLOWING DIRECTORIES:")
    print(sorted(seen_dir))
    print("\nCREATED THE FOLLOWING FILES:")
    print(sorted(seen_files))


def to_do_list():
    print("\nTO DO LIST:")
    print("\t- Add 'apps.{}' to INSTALLED APPS inside {}_main/settings.py\
        ".format(APP_NAME, PROJ_NAME))
    print("\t- Add 'url(r'^admin/', include('apps.{}.urls'), namespace='{}'),' to \
        \n\t  urls.py inside {}_main".format(APP_NAME, APP_NAME, PROJ_NAME))
    print("\t- Add the 'include' import to 'from django.conf.urls import url'\n")


if __name__ == '__main__':
    clear()
    print("--------------------------------- DJANGO PROJECT BUILDER WITH APPS ---------------------------------\n")
    PROJ_NAME = raw_input("Enter a Project Name: ")
    APP_NAME = raw_input("Enter an App Name: ")
    build_history(build_filesys())
    to_do_list()
