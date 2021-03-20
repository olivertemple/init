# init
With init you can initialise any project with a single command. It will create the directory, create a README.md with the repository name and description, as well as create a new github repository.

You will need to create an access token.

## Installation
To install, add the executable file to your python scripts folder, or another folder that is in your path environment variable.

Alternativeley you can add the folder that you save the executable file in to your path environment variable.

To do this press `win + R` and paste in `C:\Windows\System32\systempropertiesadvanced.exe` and click ok.

This will open the controll panel. Click "Environment Variables" in the bottom right corner.

In system variables, select Path and click "edit". Click new and enter the path to the folder containing the executable file.

## Usage
```
init NAME -d DESCRIPTION -p PATH -t TYPE -v --token TOKEN -f FILE
```

### Arguments
Required:
- `name`: name of the repo.

Optional:
- `--description, -d, DESCRIPTION`: brief description of the repo.
- `--path, -p, PATH`: path in which to create new repo, default is current path.
-  `--type, -t, TYPE`: directory structure to create.

    - `web`: creates a scss, css, js and assets folder. Also creates a html file with default code and links to css and js. Margins and padding set to 0 in scss file, which is compiled to css. The scss file is then watched for changes.
    ```
    REPONAME
    ├──index.html
    ├──README.md
    ├──_js
    |  └──index.js
    |
    ├──_scss
    |  └──index.scss
    |
    ├──_css
    |  └──index.css
    |
    └──_assets
    ```
    - `cmake`: creates an include and src directory. Creates an empty main.c file and a CMakeFiles.txt with the necessary information.
    ```
    REPONAME
    ├──CMakeFiles.txt
    ├──README.md
    ├──_src
    |  └──main.c
    |
    └──_include
    ```

    - `cmakepp` or `cmake++`: creates an include and src directory. Creates an empty main.cpp file and a CMakeFiles.txt with the necessary information.
    ```
    REPONAME
    ├──CMakeFiles.txt
    ├──README.md
    ├──_src
    |  └──main.cpp
    |
    └──_include
    ```

    - `rust`: creates an src folder, with the default main.rs file, as well as a Cargo.toml file (uses `cargo run` to create).
    ```
    REPONAME
    ├──README.md
    ├──Cargo.toml
    └──_src
       └──main.rs
    ```

-  `-v, --visible`: `bool` the visibility of the repository, default is private
-  `--token, TOKEN`: the guthub access token. access token will be stored as an environment variable and will be updated with this option
- `--file, -f, FILE`: create additional files. For multiple files, either use quotes or separate files by commas. `-f "index.html index.js"` or `-f index.html,index.js`

## Examples
```
init example1
```
Creates a private repository called example1 in the current directory.
```
init example2 -f main.py
```
Create a private repository called example2 in the current directory with a main.py file.
```
init example3 -d "this is a brief description for this repo" -p .\Desktop\ -t web
```
Create a private repository called example3 with a description of "this is a brief description for this repo" on the desktop using the web file structure.
```
init example3 -p C:\Users\user\Documents\ -f index.html,index.js
```
Create a private repository called example3 in the users documents with no description with 2 files index.html and index.js
```
init "example 5" -v -f "main.py requirements.txt"
```
Create a public repository called example-5 (replaces spaces with dashes) in the current directory with 2 files main.oy and requirements.txt
