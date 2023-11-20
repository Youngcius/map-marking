import time
from uiautomator2 import Device
from info import BusinessInfo

from rich.console import Console
console = Console()


def mark_amap(d: Device, info: BusinessInfo):
    """
    Mark business locations on amap (高德地图)
    """
    # 打开高德地图
    d.app_start("com.autonavi.minimap", wait=True)

    # 进入新增商家信息界面
    if not d(text='反馈').exists:
        d(text='首页').click()
    d(text='反馈').click()
    d(text="新增地点").click()

    # 输入商家名称
    while not d(text='提交').exists:
        time.sleep(0.5)
    d(text="请与门脸挂牌一致").click()
    d.send_keys(info.name, clear=True)
    d(text="创建新地点").click_gone()

    # 设置商家位置
    d(text='添加地图位置').click()
    set_pseudo_gps(d, *info.location)
    d.xpath('//*[@resource-id="com.autonavi.minimap:id/map_widget_container"]/android.widget.LinearLayout[2]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
    d(text="确定").click_gone()

    # 上传商家照片 (1~3张)
    d(text="上传图片").click()
    d(text="相册").click()
    d(text="全部").click()
    # TODO: make sure there is the corresponding album
    while not d(textStartsWith=info.identifier).exists:
        d(scrollable=True).scroll()
    d(textStartsWith=info.identifier).click()
    time.sleep(0.5)
    if (ele := d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]')).exists:
        ele.click()
    if (ele := d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]')).exists:
        ele.click()
    if (ele := d.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]')).exists:
        ele.click()
    d(textStartsWith="确定").click()

    # commit
    time.sleep(0.5)
    d(text="上传中").wait_gone()

    d(text="提交").click_gone()


def mark_bmap(d: Device, info: BusinessInfo):
    """
    Mark business locations on bmap (百度地图)
    """
    # 打开百度地图
    # TODO: 百度地图不能自动跳转到打开页面 on Android
    d.app_start("com.baidu.BaiduMap", wait=True)

    # 进入新增商家信息界面
    if not d(text="帮助反馈").exists():
        d(text='我的').click()
    d(text="帮助反馈").click()
    d(text="地点新增").click()

    # 输入商家名称
    while not d(text='提交').exists:
        time.sleep(0.5)
    d.click(0.5, 0.235)  # 请在此输入...
    # d.clipboard = info.name
    # d.long_click(0.5, 0.13)
    # d(text="粘贴").click()
    d.send_keys(info.name, clear=True)
    d(text='新增该地点').click()


    # 设置商家位置
    d(text='点击图区更改位置').click()
    set_pseudo_gps(d, *info.location)
    d(resourceId="com.baidu.BaiduMap:id/location").click()
    d(text="确认位置").click_gone()

    # 填写详细地址
    d.click(0.5, 0.34) # 详细地址
    d.send_keys(info.address, clear=True)

    # 上传商家照片 (1~3张)
    d.click(0.2, 0.6) # 上传图片
    d.click(0.5, 0.89) # 从相册上传
    d.click(0.1, 0.955) # 选择相册
    while not d(textStartsWith=info.identifier).exists:
        d(scrollable=True).scroll()
    d(textStartsWith=info.identifier).click()
    time.sleep(0.5)
    if (ele := d.xpath('//*[@resource-id="com.baidu.BaiduMap:id/myGrid"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')).exists:
        ele.click()
    if (ele := d.xpath('//*[@resource-id="com.baidu.BaiduMap:id/myGrid"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]')).exists:
        ele.click()
    if (ele := d.xpath('//*[@resource-id="com.baidu.BaiduMap:id/myGrid"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]')).exists:
        ele.click()
    d(textStartsWith="下一步").click()

    # commit
    d.swipe_ext('up')
    d.click(0.07, 0.85) # agreement terms
    d(text='提交').click_gone()


def mark_tmap(d: Device, info: BusinessInfo):
    """
    Mark business locations on tmap (腾讯地图)
    """
    # 打开腾讯地图
    d.app_start("com.tencent.map", wait=True)

    # 进入新增商家信息界面
    if not d(text="反馈").exists():
        d(text="首页").click()
    d(text="反馈").click()
    d(text="新增地点").click()
    d.click(0.5, 0.76) # skip the introduction page by clicking vacant area

    # 输入商家名称
    d.click(0.5, 0.225)  # 输入地点名称
    d.send_keys(info.name, clear=True)
    d(text='添加').click_gone()


    # 设置商家位置
    d.click(0.5, 0.45) # 在地图上选择位置
    set_pseudo_gps(d, *info.location)
    d(resourceId="com.tencent.map:id/bgq").click()
    d(text='确认选点').click_gone()

    # 填写详细地址
    d.click(0.5, 0.53) # 输入详细地址（精确到街道门牌号）
    d.send_keys(info.address, clear=True)

    # 上传商家照片 (1~3张)
    # NOTE: 腾讯地图中，只能先进入“其他相册”，在进入商家对应的相册，并且一次职能上传一张
    img_width = 0.196
    ini_x, init_y = 0.15, 0.65
    for i in range(info.num_photos):
        d.click(ini_x + i * img_width, init_y) # 上传图片
        time.sleep(0.5)
        d(text='从手机相册选择').click(timeout=1)
        d(description="更多选项").click(timeout=1)
        d.xpath('//android.widget.RelativeLayout').click(timeout=1)  # 浏览...
        d(resourceId="android:id/title", text="相册").click(timeout=1)
        time.sleep(0.5)
        d(text='相册').click(timeout=1)
        while not d(textStartsWith='其他相册').exists:
            d(scrollable=True).scroll()
        d(textStartsWith='其他相册').click()
        while not d(textStartsWith=info.identifier).exists:
            d(scrollable=True).scroll()
        d(textStartsWith=info.identifier).click()        
        d(descriptionStartsWith='照片', instance=i).click_gone()

    # contact info
    d.swipe_ext('up')
    d.click(0.5, 0.77)
    d.send_keys(info.phone, clear=True)
    # d.click(0.14, 0.77) # cancel the type-in page (unnecessary)
    
    # commit
    d(text='提交').click_gone()


def set_pseudo_gps(d: Device, longitude: float, latitude: float):
    """
    Set pseudo GPS location
    """
    # TODO: set pseudo GPS location & return back to previous APP page
    ...
