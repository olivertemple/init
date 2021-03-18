# init
With init you can initialise any project with a single command. It will create the directory, create a README.md with the repository name and description, as well as create a new github repository.

You will need to create an access token.

## Instillation
To install add the executable file to your python scripts folder, or another folder that is in your path environment variable.

Alternativeley you can add the folder that you save the executable file in to your path environment variable.

To do this press `win + R` and paste in `C:\Windows\System32\systempropertiesadvanced.exe` and click ok.

This will open the controll panel. Click "Environment Variables" in the bottom right corner.

In system variables, select Path and click "edit". Click new and enter the path to the folder containing the executable file.

## Usage
```init name description -d directory -p private -t token```

### Arguments
Required:
- `name`: name of the repositroy
- `description`: a breif description for the repository

Optional:
-  `-d, --directory, directory`: the directory in which to create the new rpository, default is your current directory
-  `-p, --private, private`: (bool) the visibility of the repository, default is private
-  `-t, --token, token`: the guthub access token. access token will be stored as an environment variable and will be updated with this option
