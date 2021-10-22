from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import numpy as np
import os
import subprocess
import requests
import time


class Wiki_FoodList_download:
    def __init__(self):
        self.Main_category_link = (
            "https://en.wikipedia.org/wiki/Lists_of_prepared_foods"
        )
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        }

    def Main_Categories_List(self, new_connection):
        """
        This method downloads the Main Food Categories from https://en.wikipedia.org/wiki/Lists_of_prepared_foods
        which will be used to download the associated sub-categories

        Parameters
        ----------
        new_connection : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        response = requests.get(self.Main_category_link, headers=self.headers)
        os.chdir("../data")

        if new_connection:
            if response.status_code == 200:
                print("Connection was successfully established with Wiki")
                page_content = response.text

                with open(
                    "Main_List_foods.html", "w", encoding="utf8"
                ) as main_food_file:
                    main_food_file.write(page_content)
                    main_food_file.close()
                print("The Main_list for food categories was successfully downloaded")
            else:
                print(
                    f"The response failed with following exit code {response.status_code}"
                )
                return

        with open("Main_List_foods.html", "r", encoding="utf8") as main_food_file:
            page_content = main_food_file.read()
            main_food_file.close()

        soup = BeautifulSoup(page_content, "html.parser")
        sub_list_content = soup.find(
            "div", attrs={"class": "mw-parser-output"}
        ).find_all("ul")

        Main_Food_Category = open("Main_Food_Categories.txt", "w")
        for instance in sub_list_content:
            list_instances = instance.find_all("li")
            for list_instance in list_instances:
                if list_instance.a.text.find("List") != -1:
                    food_type_main = list_instance.a.text
                    Main_Food_Category.write(food_type_main + "\n")
        Main_Food_Category.close()

    def Sub_Categorie_list(Main_list_name):
        pass


class Google_download:
    def __init__(self):

        self.driver = webdriver.Chrome("C:/Software/chromedriver.exe")
        self.driver.get("https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl")

    def download_images(self, key_word, number_images):
        """
        This Method downloads images for the key_word from Google Images through selium created bot

        Parameters
        ----------
        key_word : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        box = self.driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        if not os.path.isdir(f"data\{key_word}"):
            os.mkdir(f"data\{key_word}")
        box.send_keys(key_word)
        box.send_keys(Keys.ENTER)
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            for i in range(1, 10000000):
                try:
                    self.driver.find_element_by_xpath(
                        '//*[@id="islrg"]/div[1]/div[' + str(i) + "]/a[1]/div[1]/img"
                    ).screenshot(f"data\{key_word}\key_word_image+{str(i)}.png")
                    current_number_images = len(
                        [
                            name
                            for name in os.listdir(
                                os.path.join(os.getcwd(), "data", key_word)
                            )
                        ]
                    )
                    if current_number_images >= number_images:
                        break
                except:
                    pass

            if new_height == last_height or current_number_images >= number_images:
                self.driver.close()
                break
            time.sleep(2)
            last_height = new_height


if __name__ == "__main__":
    WK = Wiki_FoodList_download()
    WK.Main_Categories_List(True)
