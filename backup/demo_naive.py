import time
import uiautomator2 as u2

d = u2.connect('cb29756c')
d.implicitly_wait(10)  # 全局隐式等待 10s
# open Amap
d.app_start("com.autonavi.minimap", wait=True)


# TODO: 凡是 sleep 的地方应用 loop check 替代

# # 进入新增商家信息界面
# # d.xpath('//*[@content-desc="反馈"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
# # d.xpath('//*[@content-desc="反馈"]').click()
d(text='反馈').click()
time.sleep(1)
if d(text="新增地点").exists:
    d(text="新增地点").click()


# d.xpath('//com.autonavi.minimap.ajx3.widget.view.SpringScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

d(text="请与门脸挂牌一致").click()
d.xpath('//*[@resource-id="com.autonavi.minimap:id/mapInteractiveRelativeLayout"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').set_text('同福客栈')
d(text="创建新地点").click()

time.sleep(1)
if d(text='添加地图位置').exists:
    d(text='添加地图位置').click()
# TODO: 设置虚拟GPS
d.xpath('//*[@resource-id="com.autonavi.minimap:id/map_widget_container"]/android.widget.LinearLayout[2]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
time.sleep(3)
d(text="确定").click()


# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]')
# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]')
# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]')


# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]')
# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[2]')
# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]')

d(text="上传图片").click()
d(text="相册").click()
d(text="全部").click()
d(textContains="地图标注").click()
time.sleep(1)
d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

#TODO: select according to file names
# d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]')


d(textContains="确定").click()


# time.sleep(0.5)
# while True:
#     if(d(text="上传中").exists):
#         print("uploading...")
#         time.sleep(0.5)
#     else:
#         print("upload finished")
#         break

# use wait_gone instead
time.sleep(1)
d(text="上传中").wait_gone()

print('!!!!!!')


# # add other info (Tel, Time, etc.)
# 高德地图添加电话需要短信验证码……
# d(text="添加营业电话").click()
# d(text="添加手机号").click() # TODO: distinguish 手机 or 座机



d(text="提交").click()



# TODO: swipte by d.swipe_ext('up') or d(scrollable=True).scroll()
