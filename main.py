from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

# Entrar no Google e pesquisa a cotacao do dolar
navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

# Consulta a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
cotacao_euro = cotacao_euro.replace(",", ".")

print(cotacao_euro)

# Consulta a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(",", "")

print(cotacao_ouro)


# lê os dados da tabela do excel
tabela = pd.read_excel(r"D:\Downloads\IntensivaoPython\Aula 3\Produtos.xlsx")
# Recalcula os preços
# Atualizar cotação
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# preço de compra = cotação * preço original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

# preço de venda = preço de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

# Exporta a base atualizada
tabela.to_excel(r"D:\Downloads\IntensivaoPython\Aula 3\Tabela Atualizada.xlsx")

navegador.quit()
