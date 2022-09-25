import web_scraping as ws
import Rename as Re
import Data_Preprocess as pre


def final():
    global rename
    scrap = ws.web()
    print(scrap)
    rename = Re.Rename()
    print(rename)
    preprocess = pre.Pre_Raw()
    print(preprocess)
    return


