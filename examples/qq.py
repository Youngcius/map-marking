import uiautomator2 as u2
import time


d = u2.connect('cb29756c')



d.debug = True


d(text="QQ").click()


print(d.app_current())

time.sleep(0.5)
