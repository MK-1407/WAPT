from rich.text import Text
from rich.table import Table

# Title
Title = Text('WAPT - Windows Advanced Package Tool',style="bold")
Title.stylize('italic')
Title.justify = "center"
Title.stylize('Red')

# Help Menu
help = Table(title="HELP MENU", title_justify="center")
help.add_column('[bold Blue]Command[bold Blue]')
help.add_column('[bold red]Description[/bold red]')
help.add_row('help','Prints this help menu.', end_section=True)
help.add_row('install','Installs a package \n [bold magenta]SYNTAX:[/bold magenta] wapt install <package-name>[:version] \n [bold yellow]Example:[/bold yellow] wapt install Chrome \n          wapt install Chrome:latest \n          wapt install Chrome:72.1'
             ,end_section=True)
help.add_row('update','Updates source list of [bold Red]wapt[/bold Red].\n [bold magenta]SYNTAX:[/bold magenta] wapt update', end_section=True)
help.add_row('uninstall','Uninstalls a package. \n [bold magenta]SYNTAX:[/bold magenta] wapt uninstall <package>.\n [bold yellow]Example:[/bold yellow] wapt uninstall Chrome.')
