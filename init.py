import os
from requests import post
from json import dumps
import argparse
import subprocess


def main():
    print('''
     _       _       
    (_)     (_)  _   
     _ ____  _ _| |_ 
    | |  _ \| (_   _)
    | | | | | | | |_ 
    |_|_| |_|_|  \__)
    ''')

    parser = argparse.ArgumentParser()

    parser.add_argument("name", help="name of new repository")
    parser.add_argument(
        "description", help="description for the new repository")
    parser.add_argument("--directory", "-d",
                        help="path to create new repo, default is current path")
    parser.add_argument(
        "--private", "-p", help="bool for weather the new repository is private or not, defaults to true")
    parser.add_argument(
        "--token", "-t", help="update the stored github access token")

    args = (parser.parse_args())

    try:
        if args.token == None:
            token = os.environ['GITHUBTOKEN']
            print("using stored token...")
        else:
            print("updating stored token...")
            token = args.token
            os.system("setx GITHUBTOKEN "+token)

    except KeyError:
        if args.token == None:
            token = input("please enter your github token: ")
            os.system("setx GITHUBTOKEN "+token)
        else:
            print("updating stored token...")
            token = args.token
            os.system("setx GITHUBTOKEN "+token)

    try:
        if args.private.lower() == "false" or args.private.lower() == "f" or args.private == "0":
            private = False
        else:
            private = True
    except:
        private = True

    name = args.name
    description = args.description
    path = args.directory

    print("creating new repository ", name, "...")

    payload = {
        "name": name,
        "description": description,
        "private": private,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True}

    r = post(url="https://api.github.com/user/repos",
             data=dumps(payload), auth=("token", token))

    if r.status_code == 201:
        print("creating README.md...")
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
        os.mkdir(name)
        os.chdir("./"+name)

        file = open("README.md", "w")
        try:
            toWrite = "# "+name.split("_")+"\n"+description
        except:
            try:
                toWrite = "# "+name.split("-")+"\n"+description
            except:
                toWrite = "# "+name+"\n"+description

        file.write(toWrite)
        file.close()

        os.system("git init")
        os.system("git add README.md")
        os.system('''git commit -m "inital commit"''')

        os.system("git remote add origin https://github.com/olivertemple/"+name)
        os.system("git branch -m master main")
        os.system("git push -u origin main")
        os.popen("code .")

    elif r.status_code == 422:
        print("ERROR: repository already exists on github")
    elif r.status_code == 401:
        print("ERROR: invalid token\TRY: init name description -t token")

main()
