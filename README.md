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
```init NAME -d DESCRIPTION -p PATH -t TYPE -v --token TOKEN -f FILE```

### Arguments
Required:
- `name`: name of the repo.

Optional:
- `--description, -d, DESCRIPTION`: brief description of the repo.
- `--path, -p, PATH`: path in which to create new repo, default is current path.
-  `--type, -t, TYPE`: directory structure to create.

    - `web`: creates a scss, css, js and assets folder. Also creates a html file with default code and links to css and js. Margins and padding set to 0 in scss file, which is compiled to css. The scss file is then watched for changes.

    - `cmake`: creates an include and src directory. Creates an empty main.c file and a CMakeFiles.txt with the necessary information.

    - `cmakepp` or `cmake++`: creates an include and src directory. Creates an empty main.cpp file and a CMakeFiles.txt with the necessary information.

    - `rust`: creates an src folder, with the default main.rs file, as well as a Cargo.toml file (uses `cargo run` to create).

-  `-v, --visible`: `bool` the visibility of the repository, default is private
-  `--token, TOKEN`: the guthub access token. access token will be stored as an environment variable and will be updated with this option
- `--file, -f, FILE`: create an additional file.
