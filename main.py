from cli.menu import menuCLI
from database.connect import ConnectDatabase

#main = menuCLI()
#main.menu_principal()

def main():

    ConnectDatabase()
    menu = menuCLI()
    menu.menu_principal()


if __name__ == "__main__":
    main()
