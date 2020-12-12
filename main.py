from selenium import webdriver
import time
import random

url ="https://oxt.me/directory" 
auth_url = "https://oxt.me/auth"
fname = "out.txt"
addr_count = 1

def set_seed():
    random.seed(time.ctime())

def get_rand_delay():
    return random.randint(100,400)

def get_addr_count(fname):
    count = 0
    f = open(fname, "r")
    for line in f:
        count += 1
    f.close()
    return count

def auth(dr):
    dr.get(auth_url)
    time.sleep(4)
    login = dr.find_element_by_id("auth-login")
    login.send_keys("kirch")
    time.sleep(5)
    passwd = dr.find_element_by_id("auth-new-password")
    passwd.send_keys("!3BMwZF4nJTjkZc")
    time.sleep(2)
    login_btn = dr.find_element_by_id("signin-btn")
    login_btn.click()
    time.sleep(5)

def get_urls(begin,end,dr):
    dr.get(url)
    f_out = open("out.txt", "a")
    for i in range(begin,end):
        delay = get_rand_delay()
        print("delay = " + str(delay))
        time.sleep(delay)
        print("i = " + str(i)) 
        lst = dr.find_elements_by_css_selector("table tr td:nth-child(1) a")
        loc = lst[i].location
        s = "window.scrollTo(0, " + str(loc['y'])+")"
        dr.execute_script(s)
        lst[i].click()
        delay = get_rand_delay()
        print("delay = " + str(delay))
        time.sleep(delay)
        f_out.write(dr.current_url + "\n")
        dr.execute_script("window.history.go(-1)")
    f_out.close()

set_seed()
driver = webdriver.Firefox()
auth(driver)
driver.get(url)
count = get_addr_count(fname)
driver.get(url)
time.sleep(60)
lst = driver.find_elements_by_css_selector("table tr td:nth-child(1) a")
el_count = len(lst)
print("el_count = "+str(el_count)+"\n")
get_urls(get_addr_count(fname),el_count,driver)
driver.quit()


