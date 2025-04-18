import sys
from gestor import menu
from gestor.ui import MainWindow

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()  # Modo terminal
    else:
        app = MainWindow()  # Modo gráfico
        app.mainloop()
