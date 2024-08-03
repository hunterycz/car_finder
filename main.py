# imports
import webbrowser

from autotrader import AutoTrader
from cargurus import CarGurus
from cars_com import CarsCom
from edmunds import Edmunds


def open_web_tabs(urls: list[str]):
    '''
    Takes a list of urls strings and opens
    new tabs using chrome as the engine.
    '''
    try:
        for url in urls:
            webbrowser.get('chrome').open_new_tab(url)
            print("TABS OPEN SUCCESSFULLY!")
    except Exception as e:
        print(f"Error Occured: {e}")


# instantiate all car website classes
auto = AutoTrader()
cargurus = CarGurus()
cars = CarsCom()
edmunds = Edmunds()

# create all the urls from instances
auto_urls = auto.generate_urls()
cargurus_urls = cargurus.generate_urls()
cars_urls = cars.generate_urls()
edmunds_urls = edmunds.generate_urls()

# generate all the new tabs
open_web_tabs(auto_urls)
open_web_tabs(cargurus_urls)
open_web_tabs(cars_urls)
open_web_tabs(edmunds_urls)
