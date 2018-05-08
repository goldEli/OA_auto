# encoding: utf-8
from selenium import webdriver
import time

LOGIN_USERNAME = 'xxx'
LOGIN_PWD = 'xxx'
URL_LOGIN = "http://171.221.203.127:8989/seeyon/index.jsp"
URL_TIMESHEET = "http://171.221.203.127:8989/seeyon/collaboration/collaboration.do?method=newColl&templateId=15257636865900"
# # 工作时间
# WORK_DATE = "2018-05-09"
# # 工作内容
# WORK_CONTENT = "数博会"
# # 工作时间
# WORK_HOURS = "7"
# # 项目阶段
# WORK_PROJECT_PHASE = "项目研发阶段"
# # 子项目阶段：代码开发 需求分析
# WORK_CHILD_PROJECT_PHASE = "代码开发"
data = [
    {"WORK_DATE":"2018-05-07", "WORK_CONTENT":"数博会", "WORK_HOURS":"7", "WORK_PROJECT_PHASE":"项目研发阶段", "WORK_CHILD_PROJECT_PHASE":"代码开发"},
    {"WORK_DATE":"2018-05-08", "WORK_CONTENT":"数博会", "WORK_HOURS":"7", "WORK_PROJECT_PHASE":"项目研发阶段", "WORK_CHILD_PROJECT_PHASE":"代码开发"},
]


def main(WORK_DATE, WORK_CONTENT, WORK_HOURS, WORK_PROJECT_PHASE, WORK_CHILD_PROJECT_PHASE):
    browser = webdriver.Chrome()
    browser.get(URL_LOGIN)

    # 自动登录
    browser.find_element_by_id('login_username').send_keys(LOGIN_USERNAME)
    browser.find_element_by_id('login_password').send_keys(LOGIN_PWD)
    time.sleep(1)
    browser.find_element_by_id('login_button').click()

    # 进入工单页面
    browser.set_window_size(1200,800)
    browser.get(URL_TIMESHEET)
    browser.switch_to.frame("zwIframe")

    # 输入时间
    browser.find_element_by_id('field0002_txt').click()
    dataInputNode = browser.find_element_by_id('field0002')
    dataInputNode.clear()
    dataInputNode.send_keys(WORK_DATE)

    # 输入项目阶段
    browser.find_element_by_id('field0009_txt').click()
    browser.find_element_by_xpath("//*[@title='" +WORK_PROJECT_PHASE+"']").click()

    # 输入研发子阶段
    time.sleep(1)
    browser.find_element_by_id('field0010_txt').click()
    browser.find_element_by_xpath("//*[@title='"+WORK_CHILD_PROJECT_PHASE+"']").click()

    # 输入工作内容
    browser.find_element_by_id('field0007').send_keys(WORK_CONTENT)

    # 输入工时
    browser.find_element_by_id('field0005').send_keys(WORK_HOURS)

    # 发布
    browser.switch_to.default_content()
    browser.find_element_by_id('sendId').click()

    # 点击选择人员(选胥丽君)
    time.sleep(2)
    browser.switch_to.frame("layui-layer-iframe1")
    browser.find_element_by_id('node_15053995749591_peoples').click()

    # 选择人员
    time.sleep(2)
    browser.switch_to.default_content()
    browser.switch_to.frame("layui-layer-iframe2")
    browser.find_element_by_xpath("//*[@value='-7645841714813386337']").click()
    browser.find_element_by_xpath("//*[@class='select_selected']").click()

    # 点击确定提交
    # browser.switch_to.default_content()
    # browser.find_element_by_xpath("//div[@id='layui-layer2']/div[3]/a[1]").click()
    # browser.find_element_by_xpath("//div[@id='layui-layer1']/div[3]/a[1]").click()
    # browser.close()

if __name__ == '__main__':
    for item in data: 
        main(
            item['WORK_DATE'],
            item['WORK_CONTENT'],
            item['WORK_HOURS'],
            item['WORK_PROJECT_PHASE'],
            item['WORK_CHILD_PROJECT_PHASE']
        )

    
