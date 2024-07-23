import struct
import functions
import const


def UnpuckAllSettingBuf(self, buf):
    u_buf = []
    u_buf = struct.unpack('>4B4BHH15BI3BI2B', buf)
    print(u_buf)
    ParsAllSettings(self, u_buf)
    pass

def ParsAllSettings(self, buf):
    #проходим по всем элемнтам буфера и выставляем соответствующие значиня в GUI
    self.m_textCtrlSN_1.SetValue(str(buf[2]*256+buf[3]))
    self.m_comboBoxSS_1.SetSelection(buf[4])
    self.m_comboBoxSS_2.SetSelection(buf[5]-1)

    self.m_textCtrlSS_1.SetValue(str(buf[6]))
    self.m_textCtrlSS_2.SetValue(str(buf[7]))
    self.m_textCtrlSS_3.SetValue(str(buf[8]))
    self.m_textCtrlSS_4.SetValue(str(buf[9]))

    self.m_comboBoxSS_3.SetSelection(buf[10]-1)
    self.m_comboBoxSS_4.SetSelection(buf[11]-1)
    self.m_comboBoxSS_5.SetSelection(buf[12]-1)

    self.m_comboBoxSS_6.SetSelection(buf[13])
    self.m_comboBoxSS_7.SetSelection(buf[14])
    self.m_comboBoxSS_8.SetSelection(buf[15])

    self.m_comboBoxSS_9.SetSelection(buf[16])
    self.m_comboBoxSS_10.SetSelection(buf[17])
    self.m_comboBoxSS_11.SetSelection(buf[18])

    self.m_comboBoxSS_12.SetSelection(buf[19])
    self.m_comboBoxSS_13.SetSelection(buf[20])
    self.m_comboBoxSS_14.SetSelection(buf[21])
    self.m_comboBoxSS_15.SetSelection(buf[23])

    self.m_textCtrlMB_1.SetValue(str(buf[24]))
    self.m_comboBoxMB_1.SetSelection(self.m_comboBoxMB_1.FindString(str(buf[25])))
    stp_bits = {0x00: 0, 0x20: 1, 0x30: 2} # 0x00 - 1; 0x20 - 2; 0x30 - 1.5
    self.m_comboBoxMB_2.SetSelection(stp_bits.get(buf[27], 0))
    prt_bits = {0x00: 0, 0x04: 1, 0x06: 2} # 0x00 - none; 0x04 - even; 0x06 - odd
    self.m_comboBoxMB_3.SetSelection(prt_bits.get(buf[28], 0))
    vers = str(buf[29])
    vers_u = vers[0] + '.' + vers[1] + '.' + vers[2] + vers[3]
    functions.AddTextLog(self, 'версия прошивки: ' + vers_u + '\n')
    pass

def PuckModbusSettings(self):
    buf = []
    dev_id = int(self.m_textCtrlMB_1.GetValue())
    speed = int(self.m_comboBoxMB_1.GetValue())
    prt_bits = {0: 0x00, 1: 0x04, 2: 0x06} # 0x00 - none; 0x04 - even; 0x06 - odd
    prt = prt_bits.get(int(self.m_comboBoxMB_3.GetSelection()), 0x00)


    wordlenthbts = {0: 0x00, 1: 0x10, 2: 0x10} #0x00 - 8 bits word lenth, 0x10 - 9 bits word lenth
    wrdlenth = wordlenthbts.get(int(self.m_comboBoxMB_3.GetSelection()), 0x00)

    stop_bits = {0: 0x00, 1: 0x20, 2: 0x30}  # 0x00 - 1; 0x20 - 2; 0x30 - 1.5
    stpbits = stop_bits.get(int(self.m_comboBoxMB_2.GetSelection()), 0x00)

    buf = struct.pack('>BI3B', dev_id, speed, wrdlenth, stpbits, prt)
    #print(buf)
    return buf

def CreateBufFromWorkSettings(self):
    buf = []
    tmp = 0
    # проходим по всем элемнтам GUI и выставляем соответствующие значиня в буфер
    buf.append(self.m_comboBoxSS_1.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_2.GetCurrentSelection()+1)

    buf.append(int(self.m_textCtrlSS_1.GetValue()))

    buf.append(int(self.m_textCtrlSS_2.GetValue()))

    buf.append(int(self.m_textCtrlSS_3.GetValue()) // 256)
    buf.append(int(self.m_textCtrlSS_3.GetValue()) % 256)

    buf.append(int(self.m_textCtrlSS_4.GetValue()) // 256)
    buf.append(int(self.m_textCtrlSS_4.GetValue()) % 256)

    buf.append(self.m_comboBoxSS_3.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_4.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_5.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_6.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_7.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_8.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_9.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_10.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_11.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_12.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_13.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_14.GetCurrentSelection())
    buf.append(10)
    buf.append(self.m_comboBoxSS_15.GetCurrentSelection())
    return buf



