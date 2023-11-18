import time
import uiautomator2 as u2
from datetime import datetime
from rich.console import Console
console = Console()

#########################
# connect via USB
device = u2.connect('cb29756c')


#########################
# connect via WiFi
# device = u2.connect('http://169.231.87.203:38197')

# print device info
# console.print(device.device_info)

# app = device.app_current()

# console.print(app)


device(scrollable=True).scroll(steps=10)
# device(scrollable=True).scroll(steps=20)

# device(scrollable=True).scroll(steps=-10)


# device.screenshot('screenshot-{}.png'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')))




time.sleep(1)
