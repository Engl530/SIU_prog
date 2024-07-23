import wx as wx
import noname
import functions
from threading import Thread
import GUI_HID
import const


class Main_window(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        th1 = Thread(target=functions.ControlCurrentConnectionState, args=(self, ), daemon=True)
        th1.start()
        GUI_HID.EnableSettingsStructItems(self)
        self.OpenedFile = 0
        self.OpenedFileLenth = 0
        self.OpenedFileFullPages = 0
        self.last_page_bytes = 0

    def FileDialogOpen(self, e):
        FD = wx.FileDialog(self, "Открыть файл: ", wildcard="bin файлы (*.bin)|*bin", style=wx.FD_OPEN)
        if FD.ShowModal() == wx.ID_CANCEL:
            return
        pathname = FD.GetPath()
        f = open(pathname, 'rb')
        self.OpenedFile = f.read()
        f.close()
        self.OpenedFileLenth = len(self.OpenedFile)
        if self.OpenedFileLenth >= const.MAX_BIN_SYMBOLS:
            self.OpenedFileLenth = 0
            functions.AddTextLog(self, 'слишком большой файл прошивки\n')
            self.m_button6.Disable()
            return
        #проверка файла на совместимость с стм8
        for i in range(0,40,4):
            if self.OpenedFile[i] != 0x82:
                functions.AddTextLog(self, 'не подходящий файл\n')
                self.m_button6.Disable()
                return
        self.m_staticText401.SetLabel(pathname)
        self.m_button6.Enable()
        self.m_gauge1.Enable()
        self.OpenedFileFullPages = self.OpenedFileLenth // const.BYTES_PER_PAGE
        self.last_page_bytes = (self.OpenedFileLenth - (self.OpenedFileFullPages * const.BYTES_PER_PAGE))
        functions.AddTextLog(self, 'выбран файл:\n' + pathname + '\n')
        functions.AddTextLog(self, 'символов: ' + str(self.OpenedFileLenth))
        functions.AddTextLog(self, '\nстраниц: ' + str(self.OpenedFileFullPages + 1) + '\n')

    def SendModbusSettings(self, e):
        self.m_buttonSS_2.Disable()
        functions.SendModbusSettings(self)
        functions.sleep(0.3)
        self.m_buttonSS_2.Enable()

    def SendModbusDefaultSettings(self, e):
        functions.SendModbusDefaultSettings(self)

    def SendWorkSettings(self, e):
        functions.SendWorkSettings(self)

    def SendDefaultWorkSettings(self, e):
        functions.SendDefaultWorkSettings(self)

    def SendReadAllSettings(self, e):
        functions.SendReadAllSettings(self)

    def SendWriteSerNum(self, e):
        functions.SendWriteSerNum(self)

    def SendResetMcu(self, e):
        functions.SendResetMcu(self)

    def TextCtrlCheckDigit(self, e):
        functions.TextCtrlCheckDigit(self, e)

    def PressComButton(self, e):
        functions.PressComButton(self)

    def CheckPriority1(self, e):
        functions.CheckPriority1(self)

    def CheckPriority2(self, e):
        functions.CheckPriority2(self)

    def CheckPriority3(self, e):
        functions.CheckPriority3(self)

    def InsertPassword(self, event):
        functions.InsertPassword(self)

app = wx.App(False)
frame = Main_window(None)
frame.Show(True)
app.MainLoop()