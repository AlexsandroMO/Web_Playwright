#https://www.youtube.com/watch?v=zazI9ntX6dw
#https://www.youtube.com/watch?v=1NNMzL4W8ws
#https://playwright.dev/docs/selectors

from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd
from email.header import Header
#from tkinter import BROWSE
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://br05.greendocs.net/Itens/Pesquisa?pesquisa=MND0912&tipoItem=285&incluirTodosCampos=1&incluirConteudo=0&incluirComentario=0&manterTipoSelecionado=false&incluirComentario=%22%22&queryAvancada=&historicoQA=False&idPesquisaSalva=0&_p=71')
    page.fill("input[name='email']", 'alexsandro.oliveira@mind-infra.com')
    page.fill("input[name='password']", '01@mindmind')
    page.click("input[name='btnLogin']")
    page.locator('//*[@id="doc_480762"]').click()
    page.locator('//*[@id="showfiles"]').click()
    #page.locator('//*[@id="724858"]/td[5]/a/img').click()
    page.wait_for_timeout(50000)
    print(page.title())
    browser.close()



#<tr class="item" id="724857">


'''with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://br05.greendocs.net/Itens/Pesquisa?pesquisa=MND0912&tipoItem=285&incluirTodosCampos=1&incluirConteudo=0&incluirComentario=0&manterTipoSelecionado=false&incluirComentario=%22%22&queryAvancada=&historicoQA=False&idPesquisaSalva=0&_p=71')
    page.fill("input[name='email']", 'alexsandro.oliveira@mind-infra.com')
    page.fill("input[name='password']", '01@mindmind')
    page.click("input[name='btnLogin']")
    page.wait_for_timeout(3000)
    #page.fill(".gLFyf_gsfi", 'paçoca')
    page.click(".id='doc_488316'")
    page.wait_for_timeout(5000)
    print(page.title())
    browser.close()'''

""" 
def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.locator("text=Get Started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro")) """