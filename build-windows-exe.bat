REM command line options for building Windows executable
pyinstaller cli.py --name opcinfo --onefile --exclude-module=pytest --add-data venv\Lib\site-packages\importlib_resources\version.txt;importlib_resources --add-data opcreader\config.json;opcreader
