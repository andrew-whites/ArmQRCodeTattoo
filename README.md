To start virtual environment for API use command - "source ./Api/.env/bin/activate"

To deactivate the virtual environment use - "deactivate"

After installing anything new through pip in a virtual envirnment, always run the command - "pip freeze > ./Api/.env/requirements.txt"
This will allow the requirements file to be updated with the new modules.

to install all dependencides from the file use the command - "pip install -r ./Api/.env/requirements.txt"