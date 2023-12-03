import time


class Web:
    def __init__(self, driver):
        print('iniciando driver')
        self.driver = driver

    def open_link(self, link: str):
        self.driver.open("{}".format(link))
        time.sleep(5)

    def clickElementoPorComando(self, comand):

        if 'id' in comand:
            self.driver.clickFromXpath(comand)
            return 'xpath'
        elif '/html' in comand:
            self.driver.clickFromXpath(comand)
            return 'xpath'
        elif 'content' in comand:
            self.driver.clickFromCssSelector(comand)
            return 'css_selector'
        elif 'pdfDownloadLinkUrl' in comand:
            return self.driver.getListLink()
        elif 'finishWeb' in comand:
            print('Finalizando Web')
            self.driver.quit()
            time.sleep(3)
            print('Web finalizado')
            return 'finishWeb'
