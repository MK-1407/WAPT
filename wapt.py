import sys
from WAPT.install import install
from rich.console import Console
from WAPT.messages import Title, help

# PRINT TITLE
console = Console()
console.print(Title)

# CONSTANTS
ARGS = sys.argv
SOURCES_FILE = open("sources_list.csv")

# handle options
try:
    if len(ARGS) == 1:
        console.print(help)
    elif ARGS[1].lower() == "help":
        console.print(help)
    elif ARGS[1].lower() == "install":
        package = ARGS[2].split(':')
        package_name = package[0]
        if len(package)==2:
            package_version = ARGS[2].split(':')[1]
        else:
            package_version = None
        if package_version:
            status = install(package_name=package_name,version=package_version)
            print(status)
        else:
            status = install(package_name=package_name)
            print(status)
except Exception as e:
    print(e)

