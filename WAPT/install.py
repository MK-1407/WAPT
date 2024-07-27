from WAPT.package_downloader import download_file
from csv import reader

class Url:
    def __init__(self) -> None:
        self.url = None
        self.status = None

def get_package_url(package_name, version):
    source_file = open("C:/Users/Mayank/Programming/WAPT/sources_list.csv",'r')
    sources = list(reader(source_file))
    package_url = Url()
    for package in sources:
        if package[0] == package_name:
            package_url.url = package[1]
            package_url.status = 200
            return package_url
        else:
            package_url.status = 404
            return package_url        

def install(package_name, version='latest'):
    package_url : Url = get_package_url(package_name=package_name, version=version)
    if not package_url.status == 404:
        download_file(package_url.url)
        return "Downloaded"
    else:
        return "Not Downloaded"
