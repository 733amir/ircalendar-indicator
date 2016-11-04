from gi import require_version

require_version('Gtk', '3.0')
require_version('AppIndicator3', '0.1')

from gi.repository import Gtk
from gi.repository import AppIndicator3
from khayyam import JalaliDatetime
from os.path import abspath


id = 'ircalendar-indicator'


def menu():
    m = Gtk.Menu()
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', Gtk.main_quit)
    m.append(item_quit)
    m.show_all()
    return m


def main():
    day = JalaliDatetime.now().day
    filename = 'Icons/{}.png'.format(day)
    print(abspath(filename))
    indicator = AppIndicator3.Indicator.new(id, abspath(filename), AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    Gtk.main()

if __name__ == "__main__":
    main()
