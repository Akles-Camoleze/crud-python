import gi
import psycopg2
import configparser
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
ini_file = os.path.join(os.path.dirname(__file__), 'config.ini')

with open(ini_file, 'r') as cfg_file:
    cfg_env_txt = os.path.expandvars(cfg_file.read())

config.read_string(cfg_env_txt)

db_host = config.get('database', 'db_host')
db_user = config.get('database', 'db_user')
db_password = config.get('database', 'db_password')
db_name = config.get('database', 'db_name')
db_port = config.get('database', 'db_port')

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    print("Conexão com o PostgreSQL bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro de conexão: {e}")

window = Gtk.Window(title="Teste GTK")
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
