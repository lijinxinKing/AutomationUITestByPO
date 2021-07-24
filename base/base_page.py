'''
封装浏览器基本操作
公共方法：等待时间，截图，点击，日志，浏览器所有操作
需求：任何点击，自动去加等待时间
关键字驱动：
    公共方法关键字：
    业务关键字：操作经常绑定在一起的，封装成关键字
'''
from selenium.webdriver.common.by import By


class BasePage:
    # driver = webdriver.Chrome()
    url = 'https://account.xiaomi.com/fe/service/login/password?%3Fcallback%3Dhttp%253A%252F%252Forder.mi.com%252Flogin%252Fcallback%253Ffollowup%253Dhttps%25253A%25252F%25252Fwww.mi.com%25252F%25253Fmasid%25253D2701.0074%2526sign%253DMmExMmM4ZmJiMWE2NmM5ZDBmMjNkMmQ4ZTAwYTllNmIxZjQzNDA5Mg%252C%252C%26sid%3Dmi_eshop%26_qrsize%3D180%26_user%3D18911777318%26_bannerBiz%3Dnull=&_signature=2%26V1_passport%26H8vKY2ydSqeMDZSdub%2BvlYwexeA%3D&_result=SbNqreE9UquoJczbhM57zAsjonNQLN8S6Ji1y8PKvFkbyqBGhci%2FLaJNJZFiiQyvK4TOPgK79Q1kO7mSjNrfgC8k65O5mS%2F0Yh3U0i6yPVxe0sGEla9%2BJg21V8sYoq1YCjtd0zXfcpD0ktfHOfbKLA%3D%3D&sid=passport&qs=%253F%25253Fcallback%25253Dhttp%2525253A%2525252F%2525252Forder.mi.com%2525252Flogin%2525252Fcallback%2525253Ffollowup%2525253Dhttps%252525253A%252525252F%252525252Fwww.mi.com%252525252F%252525253Fmasid%252525253D2701.0074%25252526sign%2525253DMmExMmM4ZmJiMWE2NmM5ZDBmMjNkMmQ4ZTAwYTllNmIxZjQzNDA5Mg%2525252C%2525252C%252526sid%25253Dmi_eshop%252526_qrsize%25253D180%252526_user%25253D18911777318%252526_bannerBiz%25253Dnull%2526_result%253DSbNqreE9UquoJczbhM57zAsjonNQLN8S6Ji1y8PKvFkbyqBGhci%25252FLaJNJZFiiQyvK4TOPgK79Q1kO7mSjNrfgC8k65O5mS%25252F0Yh3U0i6yPVxe0sGEla9%25252BJg21V8sYoq1YCjtd0zXfcpD0ktfHOfbKLA%25253D%25253D%2526_signature%253D2%252526V1_passport%252526H8vKY2ydSqeMDZSdub%25252BvlYwexeA%25253D&callback=https%3A%2F%2Faccount.xiaomi.com&_sign=2%26V1_passport%26X2Z7d7uoElqKxvp7OqzQUDxI2Zs%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType='
    def __init__(self, driver):
        filePath = './tools/chromedriver.exe'
        self.driver = driver  # webdriver.Chrome(filePath)

    # 访问URL
    def visit(self):
        self.driver.get(self.url)

    # 元素的定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 元素的输入行为
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 元素的点击行为
    def click(self, loc):
        self.locator(loc).click()
