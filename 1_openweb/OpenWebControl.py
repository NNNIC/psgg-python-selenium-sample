# coding=utf-8
#ライブラリ読み込み

import time
from pathlib import Path

#selenium関連
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-application-cache')

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OpenWebControl :

    # public
    def Start(self) :
        self.Goto(self.S_START)
        return
    
    def IsEnd(self) :
        return self.CheckState(self.S_END)

    # Manager
    m_curfunc  = None
    m_nextfunc = None

    m_noWait = False

    def Update(self) :
        while(True) :
            bFirst = False
            self.m_noWait = False
            if self.m_nextfunc != None :
                self.m_curfunc = self.m_nextfunc
                self.m_nextfunc = None
                bFirst = True
                print("start of " + self.m_curfunc.__name__)

            if self.m_curfunc != None :
                self.m_curfunc(bFirst)
            
            if self.m_noWait == False :
                return

    def Goto(self,st) :
        self.m_nextfunc = st
        return

    def CheckState(self, st) :
        return self.m_curfunc == st

    def HasNextState(self) :
        return self.m_nextfunc != None

    def NoWait(self) :
        self.m_noWait = True

    #gosub
    MAX_CALL_STACK = 10
    #              1    2    3    4    5    6    7    8    9    10
    m_callstack = [None,None,None,None,None,None,None,None,None,None]
    m_callstack_level = 0 
    def GoSubState(self,sub,nex) :
        if self.m_callstack_level >= self.MAX_CALL_STACK :
            print("CALL STACK OVER FLOW")
            exit()
        self.m_callstack[self.m_callstack_level] = nex
        self.m_callstack_level = self.m_callstack_level + 1
        self.Goto(sub)

    def ReturnState(self) :
        if self.m_callstack_level <= 0 :
            print("CALL STACK UNDER FLOW")
            exit()
        self.m_callstack_level = self.m_callstack_level - 1
        st = self.m_callstack[self.m_callstack_level]
        self.Goto(st) 

    # [SYN-G-GEN OUTPUT START] indent(4) $/./$
    #             psggConverterLib.dll converted from psgg-file:OpenWebControl.psgg

    #    E_0000
    #
    m_driver = None
    m_cnt = 0
    #    S_CLICK_ENGLISH
    #    Englishへ
    def S_CLICK_ENGLISH(self,bFirst) :
        if (bFirst) :
            div = self.m_driver.find_element(By.XPATH, '//a[text()="English"]')
            div.click();
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_TRANSFER)
        return
    #    S_CLICK_JAPANESE
    #    Japaneseクリック
    def S_CLICK_JAPANESE(self,bFirst) :
        if (bFirst) :
            div = self.m_driver.find_element(By.XPATH, '//a[text()="Japanese"]')
            div.click();
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_TRANSFER4)
        return
    #    S_CLOSE
    #
    def S_CLOSE(self,bFirst) :
        if (bFirst) :
            self.m_driver.close()
        if self.HasNextState()==False :
            self.Goto(self.S_END)
        return
    #    S_END
    #
    def S_END(self, bFirst) :
        # nothing to do
        return
    #    S_INIT
    #    初期化
    def S_INIT(self,bFirst) :
        if (bFirst) :
            self.m_driver = webdriver.Chrome(options=options)
        if self.HasNextState()==False :
            self.Goto(self.S_OPEN)
        return
    #    S_INPUT_BUTTON
    #
    def S_INPUT_BUTTON(self,bFirst) :
        if (bFirst) :
            self.m_driver.find_element(By.XPATH,'//input[@type="submit"').click()
        return
    #    S_INPUT_ID
    #
    def S_INPUT_ID(self,bFirst) :
        if (bFirst) :
            self.m_driver.find_element(By.ID,'login_id').send_keys("hoge")
        if self.HasNextState()==False :
            self.Goto(self.S_INPUT_PWD)
        return
    #    S_INPUT_PWD
    #
    def S_INPUT_PWD(self,bFirst) :
        if (bFirst) :
            self.m_driver.find_element(By.ID,'password').send_keys("hoge")
        if self.HasNextState()==False :
            self.Goto(self.S_INPUT_BUTTON)
        return
    #    S_OPEN
    #
    def S_OPEN(self,bFirst) :
        if (bFirst) :
            self.m_driver.get("https://statego.programanic.com/")
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_TRANSFER5)
        return
    #    S_START
    #
    def S_START(self, bFirst) :
        self.Goto(self.S_INIT)
        self.NoWait()
        return
    #    S_WAIT_1SEC3
    #
    def S_WAIT_1SEC3(self,bFirst) :
        if (bFirst) :
            time.sleep(5)
        if self.HasNextState()==False :
            self.Goto(self.S_CLICK_ENGLISH)
        return
    #    S_WAIT_1SEC4
    #
    def S_WAIT_1SEC4(self,bFirst) :
        if (bFirst) :
            time.sleep(5)
        if self.HasNextState()==False :
            self.Goto(self.S_CLICK_JAPANESE)
        return
    #    S_WAIT_TRANSFER
    #    遷移を待つ
    def S_WAIT_TRANSFER(self,bFirst) :
        if (bFirst) :
            wait = WebDriverWait(self.m_driver, 10)  # 最大10秒間待機します
            target_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Japanese"]')))
            print("\n--------------> We are on English　page \n")
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_1SEC4)
        return
    #    S_WAIT_TRANSFER4
    #    遷移を待つ
    def S_WAIT_TRANSFER4(self,bFirst) :
        if (bFirst) :
            wait = WebDriverWait(self.m_driver, 10)  # 最大10秒間待機します90
            target_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="English"]')))
            print("\n--------------> We are on Japanse　page \n")
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_TRANSFER6)
        return
    #    S_WAIT_TRANSFER5
    #    遷移を待つ
    def S_WAIT_TRANSFER5(self,bFirst) :
        if (bFirst) :
            wait = WebDriverWait(self.m_driver, 10)  # 最大10秒間待機します
            target_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="English"]')))
            print("\n--------------> We are on Japanse　page \n")
        if self.HasNextState()==False :
            self.Goto(self.S_WAIT_1SEC3)
        return
    #    S_WAIT_TRANSFER6
    #
    def S_WAIT_TRANSFER6(self,bFirst) :
        if (bFirst) :
            self.m_cnt = self.m_cnt + 1
        if self.m_cnt < 5 :
            self.Goto( self.S_WAIT_1SEC3 )
        else :
            self.Goto( self.S_CLOSE )
        return


    # [SYN-G-GEN OUTPUT END]

# 実行
sm = OpenWebControl()
sm.Start()
while(sm.IsEnd()==False) :
    sm.Update()


    #m_bYesNo = False
    #def br_YES(self,st) :
    #    if self.HasNextState()==False :
    #        if self.m_bYesNo==True :
    #            self.Goto(st)
    #    return

    #def br_NO(self,st) :
    #    if self.HasNextState()==False :
    #        if self.m_bYesNo==False :
    #            self.Goto(st)

