import os
from requests import post
from json import dumps
import argparse
import subprocess
import threading

class thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        watchSass()

def watchSass():
    os.system("sass --no-source-map --watch ./scss/index.scss ./css/index.css --style compressed")

def main():
    print('''
     _       _       
    (_)     (_)  _   
     _ ____  _ _| |_ 
    | |  _ \| (_   _)
    | | | | | | | |_ 
    |_|_| |_|_|  \__)
    ''')

    ### get arguments from the command line
    parser = argparse.ArgumentParser()

    parser.add_argument("name", help="name of new repository")
    parser.add_argument(
        "--description", "-d", help="description for the new repository")
    parser.add_argument("--path", "-p",
                        help="path to create new repo, default is current path")
    parser.add_argument(
        "--visible", "-v", default=False, action="store_true", help="bool for weather the new repository is private or not, defaults to true")
    parser.add_argument(
        "--token", help="update the stored github access token")
    parser.add_argument("--file", "-f", help="create an additional file")
    parser.add_argument(
        "--type", "-t", help="type of file structure to initialise, web/cmake/cmakepp/rust")

    args = (parser.parse_args())

    webstack = False

    ### ensures that there are no spaces in the name
    if " " in args.name:
        args.name = "-".join(args.name.split(" "))

    ### tries to get github token from environment variables
    ###! not secure
    try:
        if args.token == None:
            ### uses stored token
            token = os.environ['GITHUBTOKEN']
            print("using stored token...")
        else:
            ### updates stored token if a new one is supplied
            print("updating stored token...")
            token = args.token
            os.popen("setx GITHUBTOKEN "+token)

    except KeyError:
        if args.token == None:
            ### prompts for access token if not available
            while True:
                token = input("please enter your github token, you can create one at https://github.com/settings/tokens/new?scopes=repo&description=init: ")
                if token != "":
                    os.popen("setx GITHUBTOKEN "+token)
                    break
                print("ERROR: no token entered")
        else:
            ## updates stored token if a new one is supplied
            print("updating stored token...")
            token = args.token
            os.popen("setx GITHUBTOKEN "+token)

    private = not args.visible

    name = args.name
    description = args.description
    path = args.path

    ### if a path is supplied, move to it
    if path != None:
        if path[0] == ".":
            if path[1] == '/' or path[1] == "\\":
                if path[2] == "/" or path[2] == "\\":
                    os.chdir(os.getcwd()+"\\"+path[2:])
                else:
                    os.chdir(os.getcwd()+"\\"+path[1:])
            else:
                os.chdir(os.getcwd()+"\\"+path)
        else:
            os.chdir(path)
    
    

    if name not in os.listdir():
        print("creating new repository ", name, "...")

        ### creates payload to post
        payload = {
            "name": name,
            "description": description,
            "private": private,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True}

        ### sends request to github to create new repo
        r = post(url="https://api.github.com/user/repos",
                    data=dumps(payload), auth=("token", token))
            
        ### if creation is successful
        if r.status_code == 201:
            ### make directory and enter it
            os.mkdir(name)
            os.chdir("./"+name)
            
            print("creating README.md...")

            ### create readme
            file = open("README.md", "w")

            if description != None:
                if "_" in description:
                    toWrite = "# "+name.split("_")+"\n"+description
                elif "-" in description:
                    toWrite = "# "+name.split("-")+"\n"+description
                else:
                    toWrite = "# "+name+"\n"+description
            else:
                if "_" in name:
                    toWrite = "# "+" ".join(name.split("_"))
                elif "-" in name:
                    toWrite = "# "+" ".join(name.split("-"))
                else:
                    toWrite = "# "+name

            file.write(toWrite)
            file.close()

            ### creates an extra file if supplied
            if args.file != None:
                if " " in args.file:
                    for item in args.file.split(" "):
                        file = open(item, "x")
                        file.close()
                elif "," in args.file:
                    for item in args.file.split(","):
                        file=open(item, "x")
                        file.close()
                else:
                    file = open(args.file, "x")
                    file.close()

            ###creates file structure if supplied
            if args.type != None:
                if args.type.lower() == "web":
                    ### web dev structure
                    #scss
                        #index.css
                    #css
                        #index.css
                    #js
                        #index.js
                    #assets
                    #index.html
                    webstack = True
                    os.mkdir("scss")
                    os.mkdir("js")
                    os.mkdir("css")
                    os.mkdir("assets")
                    file = open("index.html", "w")
                    ###fills the html file with default code
                    content = ('''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <title>'''+name+'''</title>
            <meta name="description" content="'''+(description if description != None else "")+'''">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="./css/index.css">
        </head>
        <body>
            <script src="./js/index.js" async></script>
        </body>
    </html>
                    ''')
                    file.write(content)
                    file = open("./scss/index.scss", "w")
                    ### fills scss file with default code
                    file.write('''
    * {
        margin: 0;
        padding: 0;
    }
                    ''')
                    ### create blank css and js files
                    file = open("./css/index.css", "x")
                    file = open("./js/index.js", "x")

                    ### compile scss file to css
                    os.system(
                        "sass --no-source-map ./scss/index.scss ./css/index.css --style compressed")

                elif args.type.lower() == "cmake":
                    ### c file structure
                    #include
                    #src
                        #main.c
                    #CMakeFiles.txt
                    os.mkdir("include")
                    os.mkdir("src")
                    file = open("./src/main.c", "x")
                    file = open("./CMakeFiles.txt", "w")
                    ### fill cmakefile with information
                    file.write('''
    cmake_minimum_required(VERSION 3.10)
    project('''+name+''')
    add_executable(src/main.c)
                    ''')
                    file.close()

                elif args.type.lower() == "cmake++" or args.type.lower() == "cmakepp":
                    ### c++ file structure
                    #include
                    #src
                        #main.cpp
                    #CMakeFiles.txt
                    os.mkdir("include")
                    os.mkdir("src")
                    file = open("./src/main.cpp", "x")
                    file = open("./CMakeFiles.txt", "w")
                    ### fill cmakefile with information
                    file.write('''
    cmake_minimum_required(VERSION 3.10)
    project('''+name+''')
    add_executable(src/main.cpp)
                    ''')
                    file.close()

                elif args.type.lower() == "rust" or args.type.lower() == "rs":
                    ### rust file structure
                    #src
                        #main.rs
                    #Cargo.toml
                    os.system("cargo init")

            ### initiate git repository
            os.system("git init")
            ### add files
            os.system("git add .")
            ### commit
            os.system('''git commit -m "inital commit"''')

            ### get username
            username = subprocess.check_output("git config --global user.name", shell=True).decode().rstrip()
            ### add github repository to remote
            os.system("git remote add origin https://github.com/"+username+"/"+name)
            os.system("git branch -m master main")
            os.system("git push -u origin main")

            ### watches scss if webstack has been used
            if webstack == True:
                thread().start()

            ### open vscode
            os.popen("code .")

            

        elif r.status_code == 422:
            print("ERROR: repository already exists on github")
        elif r.status_code == 401:
            print("ERROR: invalid token\TRY: init name description -t token")
    else:
        print("ERROR: {} already a directory in {}".format(name, os.getcwd()))

main()