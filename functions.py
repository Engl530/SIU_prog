import serial
from serial import tools
from serial.tools import list_ports
import const
from time import sleep
import GUI_HID
import buf_work
import re
import wx

ComButtonValue = 'поиск устройства'
CurrentConnectionState = 'Disconnected'
BusBusy = 0
CurrentSerialNumber = 0x0000
ser = serial.Serial()
ser.timeout = 0.3
ser.close()

def ControlCurrentConnectionState(self):
    global CurrentConnectionState
    global BusBusy
    global ComButtonValue
    while 1:
        if ComButtonValue == 'отключиться':
            if CurrentConnectionState == 'Connected':
                while BusBusy:
                    pass
                SendConnectionMes(self)
                if ReadConnectionMes(self) == 0:
                    CurrentConnectionState = 'Disconnected'
                    GUI_HID.HideComSettings(self)
                    GUI_HID.HideDeviseSettings(self)
                    GUI_HID.HideDeviseModbusSettings(self)
                    GUI_HID.HideSnRstSettings(self)
                    AddTextLog(self, 'отключен\n')
                    ser.close()
                sleep(0.5)
            elif CurrentConnectionState == 'Disconnected':
                ser.timeout = 0.1
                if AutoConnection(self) == 1:
                    if ComButtonValue == 'отключиться':
                        CurrentConnectionState = 'Connected'
                        GUI_HID.ShowComSettings(self, ser)
                        GUI_HID.ShowDeviseSettings(self)
                        GUI_HID.ShowDeviseModbusSettings(self)
                        GUI_HID.ShowSnRstSettings(self)
                        AddTextLog(self, 'подключен к устройству с серийным номером: ')
                        AddTextLog(self, str(CurrentSerialNumber)+'\n')
                        SendPoolAllSettings(self)
                        ReadPoolAllSettings(self)
                ser.timeout = 0.3
                sleep(0.5)
            sleep(0.5)
        elif ComButtonValue == 'поиск устройства':
            ser.close()
            sleep(0.3)
    pass

def AddTextLog(self, message):
    self.m_logTextCtrl.AppendText(message)
    pass

def AutoConnection(self):
    global ComButtonValue
    self.m_staticTextCom10.SetLabel('идет поиск')
    ports = FindComPorts(self)
    AddTextLog(self, 'найдены порты ' + str(ports) + '\n')
    for prt in ports:
        ser.close()
        ComPortSettings(prt, 9600, 'E', 1)
        if ser.is_open == False:
            try:
                ser.open()
                AddTextLog(self, 'поиск устройств в ' + str(prt) + '\n')
                for spd in const.SPEED_LIST:
                    for prty in const.PARITY_LIST:
                        for stbt in const.STOPBITS_LIST:
                            if ComButtonValue == 'поиск устройства':
                                return 0
                            ComPortSettings(prt, spd, prty, stbt)
                            if TryToConncet(self) == 1:
                                return 1
                            sleep(0.05)
                ser.close()
                AddTextLog(self, str(prt) + ' нет поддерживаемых устройств\n')
            except :
                    sleep(0.1)
                    AddTextLog(self, 'порт ' + str(prt) + ' занят \n')
                    ser.close()
    return 0

def FindComPorts(self):
    u = tools.list_ports.comports()
    p = []
    for element in u:
        p.append(element.device)
    return p

def crc16(buf, lenth):
    crc16 = 0xFFFF
    ui16 = 0xA001
    flag = 0
    i = 0
    k = 1
    while lenth != 0:
        ui16 = buf[i]
        i += 1
        k = 0
        crc16 ^= ui16
        while k < 8:
            flag = (crc16 & 1)
            crc16 >>= 1
            if flag == 1: crc16 ^= 0xA001
            k += 1
        lenth -= 1
    return crc16

def ComPortSettings(port, speed, parity, stopbits):
    ser.port = port
    ser.baudrate = speed
    ser.parity = parity
    ser.stopbits = stopbits
    pass

def TryToConncet(self):
    magic_word = []
    for w in const.magic_word:
        magic_word.append(ord(w))
        pass
    ser.write(magic_word)
    if ReadConnectionMes(self) == 1:
        return 1
    return 0

def ReadConnectionMes(self):
    buf = []
    global CurrentSerialNumber
    buf = ser.read(6)
    global BusBusy
    BusBusy = 0
    buf_len = len(buf)
    if buf_len != 0:
        if buf[const.INDEX_COMMAND] == const.COMMAND_CONNECTION and buf[const.INDEX_COMMAND_NEG] == const.COMMAND_CONNECTION_NEG:
            buf_len -= 2
            tmp = crc16(buf, buf_len)
            if buf[4] == (tmp & 0x00FF) and buf[5] == ((tmp & 0xFF00) >> 8):
                CurrentSerialNumber = (buf[const.INDEX_SERIALNUMBER_H] << 8) + (buf[const.INDEX_SERIALNUMBER_L])

                return 1
    return 0

def SendConnectionMes(self):
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    buf = []
    buf.append(const.COMMAND_CONNECTION)
    buf.append(const.COMMAND_CONNECTION_NEG)
    buf.append((CurrentSerialNumber & 0xFF00) >> 8)
    buf.append(CurrentSerialNumber & 0x00FF)
    tmp = crc16(buf, 4)
    buf.append((tmp & 0x00FF))
    buf.append((tmp & 0xFF00) >> 8)
    ser.write(buf)
    pass

def SendPoolAllSettings(self):
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    buf = []
    buf.append(const.COMMAND_READ_ALL_SETTINGS)
    buf.append(const.COMMAND_READ_ALL_SETTINGS_NEG)
    buf.append((CurrentSerialNumber & 0xFF00) >> 8)
    buf.append(CurrentSerialNumber & 0x00FF)
    tmp = crc16(buf, 4)
    buf.append((tmp & 0x00FF))
    buf.append((tmp & 0xFF00) >> 8)
    ser.write(buf)
    pass

def ReadPoolAllSettings(self):
    buf = ser.read(60)
    global BusBusy
    BusBusy = 0
    buf_len = len(buf)
    if buf_len != 0:
        if buf[const.INDEX_COMMAND] == const.COMMAND_READ_ALL_SETTINGS and buf[const.INDEX_COMMAND_NEG] == const.COMMAND_READ_ALL_SETTINGS_NEG:
            buf_len -= 2
            tmp = crc16(buf, buf_len)
            tmp1 = buf_len
            tmp2 = buf_len+1
            if buf[tmp1] == (tmp & 0x00FF) and buf[tmp2] == ((tmp & 0xFF00) >> 8):
                AddTextLog(self, 'настройки считаны успешно\n')
                buf_work.UnpuckAllSettingBuf(self, buf)
                return 1
    return 0
    pass

def SendModbusSettings(self):
    CheckValueTextCtrl(self)
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    Rxbuf = []
    Txbuf = []
    Txbuf.append(const.COMMAND_WRITE_UART_SETTINGS)
    Txbuf.append(const.COMMAND_WRITE_UART_SETTINGS_NEG)
    Txbuf.append((CurrentSerialNumber & 0xFF00) >> 8)
    Txbuf.append(CurrentSerialNumber & 0x00FF)
    for element in buf_work.PuckModbusSettings(self):
        Txbuf.append(element)
    tmp = crc16(Txbuf, len(Txbuf))
    Txbuf.append((tmp & 0x00FF))
    Txbuf.append((tmp & 0xFF00) >> 8)
    print(Txbuf)
    ser.write(Txbuf)
    Rxbuf = ser.read(60)
    BusBusy = 0
    Rxbuf_len = len(Rxbuf)
    if Rxbuf_len != 0:
        if Rxbuf[const.INDEX_COMMAND] == const.COMMAND_WRITE_UART_SETTINGS and Rxbuf[const.INDEX_COMMAND_NEG] == const.COMMAND_WRITE_UART_SETTINGS_NEG:
            Rxbuf_len -= 2
            tmp = crc16(Rxbuf, Rxbuf_len)
            tmp1 = Rxbuf_len
            tmp2 = Rxbuf_len+1
            if Rxbuf[tmp1] == (tmp & 0x00FF) and Rxbuf[tmp2] == ((tmp & 0xFF00) >> 8):
                AddTextLog(self, 'настройки записаны успешно\n')
                return 1
    AddTextLog(self, 'настройки не записаны\n')
    return 0
    pass

def SendModbusDefaultSettings(self):
    GUI_HID.ShowDefaultModbusSetting(self)
    SendModbusSettings(self)
    pass

def SendWorkSettings(self):
    CheckValueTextCtrl(self)
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    Rxbuf = []
    Txbuf = []
    Txbuf.append(const.COMMAND_WRITE_WORK_SETTINGS)
    Txbuf.append(const.COMMAND_WRITE_WORK_SETTINGS_NEG)
    Txbuf.append((CurrentSerialNumber & 0xFF00) >> 8)
    Txbuf.append(CurrentSerialNumber & 0x00FF)
    for element in buf_work.CreateBufFromWorkSettings(self):
        Txbuf.append(element)
    tmp = crc16(Txbuf, len(Txbuf))
    Txbuf.append((tmp & 0x00FF))
    Txbuf.append((tmp & 0xFF00) >> 8)
    print(Txbuf)
    ser.write(Txbuf)
    Rxbuf = ser.read(60)
    BusBusy = 0
    Rxbuf_len = len(Rxbuf)
    if Rxbuf_len != 0:
        if Rxbuf[const.INDEX_COMMAND] == const.COMMAND_WRITE_WORK_SETTINGS and Rxbuf[
            const.INDEX_COMMAND_NEG] == const.COMMAND_WRITE_WORK_SETTINGS_NEG:
            Rxbuf_len -= 2
            tmp = crc16(Rxbuf, Rxbuf_len)
            tmp1 = Rxbuf_len
            tmp2 = Rxbuf_len + 1
            if Rxbuf[tmp1] == (tmp & 0x00FF) and Rxbuf[tmp2] == ((tmp & 0xFF00) >> 8):
                AddTextLog(self, 'настройки записаны успешно\n')
                return 1
    AddTextLog(self, 'настройки не записаны\n')
    return 0
    pass

def SendDefaultWorkSettings(self):
    self.m_buttonSS_1.Disable()
    GUI_HID.ShowDefaultWorkSetting(self)
    SendWorkSettings(self)
    sleep(0.3)
    self.m_buttonSS_1.Enable()
    pass

def SendReadAllSettings(self):
    SendPoolAllSettings(self)
    ReadPoolAllSettings(self)
    pass

def SendWriteSerNum(self):
    CheckValueTextCtrl(self)
    global CurrentSerialNumber
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    Txbuf = []
    Txbuf.append(const.COMMAND_WRITE_SERIAL_NUMBER)
    Txbuf.append(const.COMMAND_WRITE_SERIAL_NUMBER_NEG)
    Txbuf.append((CurrentSerialNumber & 0xFF00) >> 8)
    Txbuf.append(CurrentSerialNumber & 0x00FF)
    new_serial_number = int(self.m_textCtrlSN_1.GetValue())
    Txbuf.append((new_serial_number & 0xFF00) >> 8)
    Txbuf.append(new_serial_number & 0x00FF)
    tmp = crc16(Txbuf, len(Txbuf))
    Txbuf.append((tmp & 0x00FF))
    Txbuf.append((tmp & 0xFF00) >> 8)
    ser.write(Txbuf)
    Rxbuf = ser.read(10)
    BusBusy = 0
    Rxbuf_len = len(Rxbuf)
    if Rxbuf_len != 0:
        if Rxbuf[const.INDEX_COMMAND] == const.COMMAND_WRITE_SERIAL_NUMBER and Rxbuf[
            const.INDEX_COMMAND_NEG] == const.COMMAND_WRITE_SERIAL_NUMBER_NEG:
            Rxbuf_len -= 2
            tmp = crc16(Rxbuf, Rxbuf_len)
            if Rxbuf[6] == (tmp & 0x00FF) and Rxbuf[7] == ((tmp & 0xFF00) >> 8):
                CurrentSerialNumber = (Rxbuf[4] << 8) + (Rxbuf[5])
                AddTextLog(self, 'записан серийный номер: ' + str(CurrentSerialNumber)+'\n')
                return 1
    AddTextLog(self, 'не удалось записать серийный номер')
    return 0

def SendResetMcu(self):
    global CurrentSerialNumber
    global BusBusy
    while BusBusy:
        pass
    BusBusy = 1
    Txbuf = []
    Txbuf.append(const.COMMAND_RESET_MCU)
    Txbuf.append(const.COMMAND_RESET_MCU_NEG)
    Txbuf.append((CurrentSerialNumber & 0xFF00) >> 8)
    Txbuf.append(CurrentSerialNumber & 0x00FF)
    tmp = crc16(Txbuf, len(Txbuf))
    Txbuf.append((tmp & 0x00FF))
    Txbuf.append((tmp & 0xFF00) >> 8)
    ser.write(Txbuf)
    Rxbuf = ser.read(12)
    BusBusy = 0
    Rxbuf_len = len(Rxbuf)
    if Rxbuf_len != 0:
        if Rxbuf[const.INDEX_COMMAND] == const.COMMAND_RESET_MCU and Rxbuf[
            const.INDEX_COMMAND_NEG] == const.COMMAND_RESET_MCU_NEG:
            Rxbuf_len -= 2
            tmp = crc16(Rxbuf, Rxbuf_len)
            if Rxbuf[Rxbuf_len] == (tmp & 0x00FF) and Rxbuf[Rxbuf_len+1] == ((tmp & 0xFF00) >> 8):
                AddTextLog(self, 'перезагрузка MCU\n')
                return 1
    AddTextLog(self, 'нет ответа на команду\n')
    return 0
    pass

def TextCtrlCheckDigit(self, event):
    tmp_obj = event.EventObject
    tmp_str = tmp_obj.GetValue()
    for char in tmp_str:
        if char.isdigit() == False:
            new_str = tmp_str.replace(char, '')
            tmp_obj.SetValue(new_str)
    pass

def CheckValueTextCtrl(self):
    try:
        if int(self.m_textCtrlSS_1.GetValue()) > const.BRIGHTNESS_MAX_VALUE:
            self.m_textCtrlSS_1.SetValue(str(const.BRIGHTNESS_MAX_VALUE))
        elif int(self.m_textCtrlSS_1.GetValue()) < const.BRIGHTNESS_MIN_VALUE:
            self.m_textCtrlSS_1.SetValue(str(const.BRIGHTNESS_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    try:
        if int(self.m_textCtrlSS_2.GetValue()) > const.LED_SPEED_MAX_VALUE:
            self.m_textCtrlSS_2.SetValue(str(const.LED_SPEED_MAX_VALUE))
        elif int(self.m_textCtrlSS_2.GetValue()) < const.LED_SPEED_MIN_VALUE:
            self.m_textCtrlSS_2.SetValue(str(const.LED_SPEED_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    try:
        if int(self.m_textCtrlSS_3.GetValue()) > const.BUZZER_ON_TIME_MAX_VALUE:
            self.m_textCtrlSS_3.SetValue(str(const.BUZZER_ON_TIME_MAX_VALUE))
        elif int(self.m_textCtrlSS_3.GetValue()) < const.BUZZER_ON_TIME_MIN_VALUE:
            self.m_textCtrlSS_3.SetValue(str(const.BUZZER_ON_TIME_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    try:
        if int(self.m_textCtrlSS_4.GetValue()) > const.BUZZER_OFF_TIME_MAX_VALUE:
            self.m_textCtrlSS_4.SetValue(str(const.BUZZER_OFF_TIME_MAX_VALUE))
        elif int(self.m_textCtrlSS_4.GetValue()) < const.BUZZER_OFF_TIME_MIN_VALUE:
            self.m_textCtrlSS_4.SetValue(str(const.BUZZER_OFF_TIME_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    try:
        if int(self.m_textCtrlMB_1.GetValue()) > const.OWN_ID_MAX_VALUE:
            self.m_textCtrlMB_1.SetValue(str(const.OWN_ID_MAX_VALUE))
        elif int(self.m_textCtrlMB_1.GetValue()) < const.OWN_ID_MIN_VALUE:
            self.m_textCtrlMB_1.SetValue(str(const.OWN_ID_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    try:
        if int(self.m_textCtrlSN_1.GetValue()) > const.SERIAL_NUM_MAX_VALUE:
            self.m_textCtrlSN_1.SetValue(str(const.SERIAL_NUM_MAX_VALUE))
        elif int(self.m_textCtrlSN_1.GetValue()) < const.SERIAL_NUM_MIN_VALUE:
            self.m_textCtrlSN_1.SetValue(str(const.SERIAL_NUM_MIN_VALUE))
    except ValueError:
        self.m_textCtrlSS_1.SetValue(str(0))
    pass

def PressComButton(self):
    global CurrentConnectionState
    self.m_buttonCOM_1.Disable()
    global ComButtonValue
    if ComButtonValue == 'поиск устройства':
        ComButtonValue = 'отключиться'
        self.m_buttonCOM_1.SetLabel(ComButtonValue)
        sleep(0.3)
        self.m_buttonCOM_1.Enable()
        return
    elif ComButtonValue == 'отключиться':
        ComButtonValue = 'поиск устройства'

        GUI_HID.HideComSettings(self)
        GUI_HID.HideDeviseSettings(self)
        GUI_HID.HideDeviseModbusSettings(self)
        GUI_HID.HideSnRstSettings(self)
        AddTextLog(self, 'отключен\n')
        CurrentConnectionState = 'Disconnected'

        self.m_buttonCOM_1.SetLabel(ComButtonValue)
        sleep(0.3)
        self.m_buttonCOM_1.Enable()
        return
    pass

def CheckPriority1(self):
    a = [0, 1, 2]
    tmp = self.m_comboBoxSS_3.GetSelection()
    a.remove(tmp)
    if self.m_comboBoxSS_4.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_5.GetSelection())
        self.m_comboBoxSS_4.SetSelection(a[0])
    if self.m_comboBoxSS_5.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_4.GetSelection())
        self.m_comboBoxSS_5.SetSelection(a[0])
    pass

def CheckPriority2(self):
    a = [0, 1, 2]
    tmp = self.m_comboBoxSS_4.GetSelection()
    a.remove(tmp)
    if self.m_comboBoxSS_3.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_5.GetSelection())
        self.m_comboBoxSS_3.SetSelection(a[0])
    if self.m_comboBoxSS_5.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_3.GetSelection())
        self.m_comboBoxSS_5.SetSelection(a[0])
    pass

def CheckPriority3(self):
    a = [0, 1, 2]
    tmp = self.m_comboBoxSS_5.GetSelection()
    a.remove(tmp)
    if self.m_comboBoxSS_3.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_4.GetSelection())
        self.m_comboBoxSS_3.SetSelection(a[0])
    if self.m_comboBoxSS_4.GetSelection() == tmp:
        a.remove(self.m_comboBoxSS_3.GetSelection())
        self.m_comboBoxSS_4.SetSelection(a[0])
    pass

def InsertPassword(self):
    global CurrentConnectionState
    n = self.m_checkBox1.GetValue()
    if n == True:
        self.m_checkBox1.SetValue(False)
        PD = wx.PasswordEntryDialog(self, message='Введите пароль', caption='Ввод пароля')
        if PD.ShowModal() == wx.ID_CANCEL:
            return
        elif wx.ID_OK:
            if PD.GetValue() == const.password_to_change_serial:
                AddTextLog(self, 'Пароль верный\n')
                self.m_checkBox1.SetValue(True)
                if CurrentConnectionState == 'Connected':
                    self.m_textCtrlSN_1.Enabled = True
                    self.m_buttonSN_2.Enabled = True
            else:
                AddTextLog(self, 'Введен неверный пароль\n')
            return
    else:
        self.m_textCtrlSN_1.Enabled = False
        self.m_buttonSN_2.Enabled = False
    pass