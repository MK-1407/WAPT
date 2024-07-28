import csv


def search(package_name):
    sources_file = open("C:/Users/Mayank/Programming/wapt/sources_list.csv")
    sources = list(csv.reader(sources_file))
    for package in sources:
        if package_name == package[0]:
            return {"name":package[0],"url":package[1],"version":package[3]}
        else:
            return "Package not found"
    