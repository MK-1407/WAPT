# WAPT - Windows Advanced Package Tool
> WAPT is in development phase and even all basic functionality are being added.
> Currently it has only one functionality, install, which only downloads the package
> from sources.

WAPT or WinApt or Windows Advanced Package Tool is an package manager for Windows inspired from Debian's Advanced Package Tool or apt. WAPT is packed with the simplicity and super cow powers of apt, still with slight difference in the backend architecture.

## Installation

- Clone this repository.
```
git clone https://github.com/MK-1407/WAPT.git
```
- Install required libraries.
```
python -m pip install -r requirements.txt
```

## Usage
Make sure you are in the same directory as wapt.py then run
```
python wapt.py
```
You would see the help menu of WAPT.
- Installing a package.
```
python wapt.py install <package-name>[:version]
```
- Print the help menu
```
python wapt.py help
```
- Searching for a package
```
python wapt.py search <package-name>[:version]
```
- Updating Source list
```
python wapt.py update
```

## Wapt Source List

You can look at Wapt's source list [here](./sources_list.csv)
Wapt is in development, your contribution  would be valuable. So if you can please add packages to the source list, the format for it is.

```
Package name,package url,latest,version.
```

## Contributing
No pull request will be accepted to main branch. So please create a separate branch which will be merged after review.