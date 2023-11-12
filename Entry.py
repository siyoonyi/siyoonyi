class comment():
    def Start(Entry_id, Entry_pw, ProjectUrl, YourComment, repeat):

        from selenium.webdriver.common.by import By
        from selenium import webdriver
        import time
        import chromedriver_autoinstaller

        def wait(DriverWait, TimeSleep):
            driver.implicitly_wait(DriverWait)
            time.sleep(TimeSleep)

        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.get(url="https://playentry.org")
        wait(10, 1)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div/div/div[2]/a/div').click()
        wait(10, 1)
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(Entry_id)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Entry_pw)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/section/div/div[2]/div/a').click()
        wait(10, 5)

        #Comment Start:

        driver.get(ProjectUrl)

        wait(10, 3)
        written = 0
        if repeat == 0:
            while True:
                driver.find_element(By.XPATH, '//*[@id="Write"]').send_keys(YourComment)
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[1]/div[6]/div/div[1]/div[2]/span/a').click()
                written = written+1
                print("LOG || Comment will be written again in 1 min.   ", written, "time(s) written")
                time.sleep(60)

        else:
            for i in range(repeat):
                driver.find_element(By.XPATH, '//*[@id="Write"]').send_keys(YourComment)
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[1]/div[6]/div/div[1]/div[2]/span/a').click()
                print("LOG || Comment will be written again in 1 min")
                time.sleep(60)

class talk():
    def Start(Entry_id, Entry_pw, Talk, repeat):

        from selenium.webdriver.common.by import By
        from selenium import webdriver
        import time
        import chromedriver_autoinstaller

        def wait(DriverWait, TimeSleep):
            driver.implicitly_wait(DriverWait)
            time.sleep(TimeSleep)

        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.get(url="https://playentry.org")
        wait(10, 1)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div/div/div[2]/a/div').click()
        wait(10, 1)
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(Entry_id)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Entry_pw)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/section/div/div[2]/div/a').click()
        wait(10, 5)

        #talk start

        driver.get('https://playentry.org/community/entrystory/list?sort=created&term=all')

        wait(10, 3)
        written = 0
        if repeat == 0:
            while True:
                driver.find_element(By.XPATH, '//*[@id="Write"]').send_keys(Talk)
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/section/div/div[2]/div/div[1]/div/div[1]/span/a').click()
                written = written+1
                print("LOG || Comment will be written again in 2 min.   ", written, "time(s) written")
                time.sleep(120)

        else:
            for i in range(repeat):
                driver.find_element(By.XPATH, '//*[@id="Write"]').send_keys(Talk)
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/section/div/div[2]/div/div[1]/div/div[1]/span/a').click()
                print("LOG || Comment will be written again in 2 min")
                time.sleep(120)