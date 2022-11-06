
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#ブラウザを立ち上げる
# browser = webdriver.Chrome(ChromeDriverManager().install())

#サイトにアクセス 引数にurlを記載
browser.get("https://www.yahoo.co.jp/")

#yohooの検索ボックスに検索ワードを記入 
# 検索ボックスはfind_elemwntメソッドを使い指定する 引数はサイトのhtmlを参照
box = browser.find_element(By.NAME, "p")
box.send_keys("AWS")

#検索ボタンをXpathで指定し検索
search_button = browser.find_element(By.XPATH, "/html/body/div/div/header/section[1]/div/form/fieldset/span/button")
search_button.click()

#検索ボタンのxpath(htmlの属性を一意に決定) 
# /html/body/div/div/header/section[1]/div/form/fieldset/span/button

#ブラウザを閉じる
browser.close()

