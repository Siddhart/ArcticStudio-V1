from selenium import webdriver
import time
from flask import Flask
import json

app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

google = webdriver.Chrome(chrome_options=options)

@app.route("/api/epicGames/free")
def getFreeGames():
    google.get("https://www.epicgames.com/store/en-US/")

    time.sleep(10)
    name1 = ''
    imgURL1 = ''
    freeUntil1 = ''
    url1 = ''
    name2 = ''
    imgURL2 = ''
    freeUntil2 = ''
    url2 = ''
    name3 = ''
    imgURL3 = ''
    freeUntil3 = ''
    url3 = ''

    try:
        name1 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[1]/div/a/div/div/div[2]/span[1]').text
        imgURL1 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[1]/div/a/div/div/div[1]/div/div/img').get_attribute("data-image")
        freeUntil1 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[1]/div/a/div/div/div[2]/span[2]/span/time[1]').text
        url1 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[1]/div/a').get_attribute("href")
    except:
        print("xpath broke!")
    
    try:
        free2 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[2]/div/a/div/div/div[1]/span').text
        if free2 == "FREE NOW":
            name2 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[2]/div/a/div/div/div[2]/span[1]').text
            imgURL2 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[2]/div/a/div/div/div[1]/div/div/img').get_attribute("data-image")
            freeUntil2 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[2]/div/a/div/div/div[2]/span[2]/span/time[1]').text
            url2 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[2]/div/a').get_attribute("href")
        else:
            print('no second offer!')
    except:
        print("xpath broke!")

    try:
        free3 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[3]/div/a/div/div/div[1]/span').text
        if free3 == "FREE NOW":
            name3 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[3]/div/a/div/div/div[2]/span[1]').text
            imgURL3 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[3]/div/a/div/div/div[1]/div/div/img').get_attribute("data-image")
            freeUntil3 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[3]/div/a/div/div/div[2]/span[2]/span/time[1]').text
            url3 = google.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/section[2]/div/span/div/section/div/div[3]/div/a').get_attribute("href")
        else:
            print('no third offer!')
    except:
        print("xpath broke!")

    x = {
        "games":
        [
            {"name": name1, "until": freeUntil1, "imageurl": imgURL1, "url": url1},
            {"name": name2, "until": freeUntil2, "imageurl": imgURL2, "url": url2},
            {"name": name3, "until": freeUntil3, "imageurl": imgURL3, "url": url3}
        ]
    }

    realJson = json.dumps(x, indent=3)

    return realJson

if __name__ == "__main__":
    app.run(port=88, host='192.168.178.24')
