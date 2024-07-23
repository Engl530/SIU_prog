# тут все функции для отображения в гуи
import const

def EnableSettingsStructItems(self):

    pass

def ShowComSettings(self, ser):
    self.m_staticTextCom6.SetLabel(ser.port)
    self.m_staticTextCom7.SetLabel(str(ser.baudrate))
    if ser.parity == 'N':
        self.m_staticTextCom8.SetLabel('нет')
    elif ser.parity == 'E':
        self.m_staticTextCom8.SetLabel('чет')
    elif ser.parity == 'O':
        self.m_staticTextCom8.SetLabel('нечет')
    self.m_staticTextCom9.SetLabel(str(ser.stopbits))
    self.m_staticTextCom10.SetLabel('подключен')
    pass

def HideComSettings(self):
    self.m_staticTextCom6.SetLabel('--')
    self.m_staticTextCom7.SetLabel('--')
    self.m_staticTextCom8.SetLabel('--')
    self.m_staticTextCom9.SetLabel('--')
    self.m_staticTextCom10.SetLabel('--')
    pass

def ShowDeviseSettings(self):
    self.m_comboBoxSS_1.Enabled = True
    self.m_comboBoxSS_2.Enabled = True
    self.m_comboBoxSS_3.Enabled = True
    self.m_comboBoxSS_4.Enabled = True
    self.m_comboBoxSS_5.Enabled = True
    self.m_comboBoxSS_6.Enabled = True
    self.m_comboBoxSS_7.Enabled = True
    self.m_comboBoxSS_8.Enabled = True
    self.m_comboBoxSS_9.Enabled = True
    self.m_comboBoxSS_10.Enabled = True
    self.m_comboBoxSS_11.Enabled = True
    self.m_comboBoxSS_12.Enabled = True
    self.m_comboBoxSS_13.Enabled = True
    self.m_comboBoxSS_14.Enabled = True
    self.m_comboBoxSS_15.Enabled = True
    self.m_buttonSS_1.Enabled = True
    self.m_buttonSS_2.Enabled = True
    self.m_textCtrlSS_1.Enabled = True
    self.m_textCtrlSS_2.Enabled = True
    self.m_textCtrlSS_3.Enabled = True
    self.m_textCtrlSS_4.Enabled = True
    if self.m_checkBox1.GetValue() == True:
        self.m_textCtrlSN_1.Enabled = True
        self.m_buttonSN_2.Enabled = True

    pass

def HideDeviseSettings(self):
    self.m_comboBoxSS_1.Enabled = False
    self.m_comboBoxSS_2.Enabled = False
    self.m_comboBoxSS_3.Enabled = False
    self.m_comboBoxSS_4.Enabled = False
    self.m_comboBoxSS_5.Enabled = False
    self.m_comboBoxSS_6.Enabled = False
    self.m_comboBoxSS_7.Enabled = False
    self.m_comboBoxSS_8.Enabled = False
    self.m_comboBoxSS_9.Enabled = False
    self.m_comboBoxSS_10.Enabled = False
    self.m_comboBoxSS_11.Enabled = False
    self.m_comboBoxSS_12.Enabled = False
    self.m_comboBoxSS_13.Enabled = False
    self.m_comboBoxSS_14.Enabled = False
    self.m_comboBoxSS_15.Enabled = False
    self.m_buttonSS_1.Enabled = False
    self.m_buttonSS_2.Enabled = False
    self.m_textCtrlSS_1.Enabled = False
    self.m_textCtrlSS_2.Enabled = False
    self.m_textCtrlSS_3.Enabled = False
    self.m_textCtrlSS_4.Enabled = False
    pass

def ShowDeviseModbusSettings(self):
    self.m_textCtrlMB_1.Enabled = True
    self.m_comboBoxMB_1.Enabled = True
    self.m_comboBoxMB_2.Enabled = True
    self.m_comboBoxMB_3.Enabled = True
    self.m_buttonMB_1.Enabled = True
    self.m_buttonMB_2.Enabled = True
    pass

def HideDeviseModbusSettings(self):
    self.m_textCtrlMB_1.Enabled = False
    self.m_comboBoxMB_1.Enabled = False
    self.m_comboBoxMB_2.Enabled = False
    self.m_comboBoxMB_3.Enabled = False
    self.m_buttonMB_1.Enabled = False
    self.m_buttonMB_2.Enabled = False
    pass

def ShowDefaultModbusSetting(self):
    self.m_textCtrlMB_1.SetValue(str(const.DEFAULT_UART_OWN_ID))
    self.m_comboBoxMB_1.SetSelection(2)
    self.m_comboBoxMB_2.SetSelection(0)
    self.m_comboBoxMB_3.SetSelection(1)
    pass

def ShowDefaultWorkSetting(self):
    self.m_comboBoxSS_1.SetSelection(0)
    self.m_comboBoxSS_2.SetSelection(3)

    self.m_textCtrlSS_1.SetValue(str(const.DEFAULT_BRIGHTNESS))
    self.m_textCtrlSS_2.SetValue(str(const.DEFAULT_LED_SPEED))
    self.m_textCtrlSS_3.SetValue(str(const.DEFAULT_BUZZER_ON_TIME))
    self.m_textCtrlSS_4.SetValue(str(const.DEFAULT_BUZZER_OFF_TIME))

    self.m_comboBoxSS_3.SetSelection(2)
    self.m_comboBoxSS_4.SetSelection(1)
    self.m_comboBoxSS_5.SetSelection(0)

    self.m_comboBoxSS_6.SetSelection(0)
    self.m_comboBoxSS_7.SetSelection(1)
    self.m_comboBoxSS_8.SetSelection(1)

    self.m_comboBoxSS_9.SetSelection(1)
    self.m_comboBoxSS_10.SetSelection(0)
    self.m_comboBoxSS_11.SetSelection(0)

    self.m_comboBoxSS_12.SetSelection(1)
    self.m_comboBoxSS_13.SetSelection(0)
    self.m_comboBoxSS_14.SetSelection(0)
    self.m_comboBoxSS_15.SetSelection(1)
    pass

def ShowSnRstSettings(self):
    #self.m_textCtrlSN_1.Enabled = True
    self.m_buttonSN_1.Enabled = True
    #self.m_buttonSN_2.Enabled = True
    self.m_buttonRST_1.Enabled = True
    if self.m_checkBox1.GetValue() == True:
        self.m_textCtrlSN_1.Enabled = True

    pass

def HideSnRstSettings(self):
    self.m_textCtrlSN_1.Enabled = False
    self.m_buttonSN_1.Enabled = False
    self.m_buttonSN_2.Enabled = False
    self.m_buttonRST_1.Enabled = False
    pass