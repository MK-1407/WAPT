import csv


def search(package_name):
    sources_file = open("C:/Users/Mayank/Programming/wapt/sources_list.csv")
    sources = list(csv.reader(sources_file))
    packages = []
    for package in sources:
        if package_name.lower() == package[0].lower():
            packages.append({"name":package[0],"url":package[1],"version":package[3]})
        else:
            return "Package not found"
    return packages