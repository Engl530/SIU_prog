# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1190,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1190,700 ), wx.DefaultSize )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2.SetMinSize( wx.Size( 500,400 ) ) 
		self.m_logTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,600 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		self.m_logTextCtrl.SetMinSize( wx.Size( 300,400 ) )
		self.m_logTextCtrl.SetMaxSize( wx.Size( 600,-1 ) )
		
		bSizer2.Add( self.m_logTextCtrl, 1, wx.ALL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextCom1 = wx.StaticText( self, wx.ID_ANY, u"Текущие настройки COM порта:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom1.Wrap( -1 )
		bSizer9.Add( self.m_staticTextCom1, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 2, 6, 0, 0 )
		
		self.m_staticTextCom2 = wx.StaticText( self, wx.ID_ANY, u"порт:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom2.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom2, 0, wx.ALL, 5 )
		
		self.m_staticTextCom3 = wx.StaticText( self, wx.ID_ANY, u"скорость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom3.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom3, 0, wx.ALL, 5 )
		
		self.m_staticTextCom4 = wx.StaticText( self, wx.ID_ANY, u"четность:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom4.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom4, 0, wx.ALL, 5 )
		
		self.m_staticTextCom5 = wx.StaticText( self, wx.ID_ANY, u"стоп-биты:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom5.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom5, 0, wx.ALL, 5 )
		
		self.m_staticTextCom5 = wx.StaticText( self, wx.ID_ANY, u"состояние:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom5.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom5, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer2.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_staticTextCom6 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom6.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom6, 0, wx.ALL, 5 )
		
		self.m_staticTextCom7 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom7.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom7, 0, wx.ALL, 5 )
		
		self.m_staticTextCom8 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom8.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom8, 0, wx.ALL, 5 )
		
		self.m_staticTextCom9 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom9.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom9, 0, wx.ALL, 5 )
		
		self.m_staticTextCom10 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom10.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom10, 0, wx.ALL, 5 )
		
		self.m_buttonCOM_1 = wx.Button( self, wx.ID_ANY, u"поиск устройства", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_buttonCOM_1, 1, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer2, 0, 0, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer21 = wx.GridSizer( 21, 2, 1, 0 )
		
		gSizer21.SetMinSize( wx.Size( 400,400 ) ) 
		self.m_staticTextSS_1 = wx.StaticText( self, wx.ID_ANY, u"Настройки режима работы:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_1.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_1, 0, wx.ALL, 5 )
		
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		gSizer21.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_2 = wx.StaticText( self, wx.ID_ANY, u"источник управления:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_2.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_2, 0, wx.ALL, 5 )
		
		m_comboBoxSS_1Choices = [ u"входы", u"MODBUS", u"смешанный" ]
		self.m_comboBoxSS_1 = wx.ComboBox( self, wx.ID_ANY, u"входы", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_1Choices, wx.CB_READONLY )
		self.m_comboBoxSS_1.SetSelection( 0 )
		self.m_comboBoxSS_1.Enable( False )
		self.m_comboBoxSS_1.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_1, 0, 0, 5 )
		
		self.m_staticTextSS_3 = wx.StaticText( self, wx.ID_ANY, u"кол-во бегущих светодиодов:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_3.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_3, 0, wx.ALL, 5 )
		
		m_comboBoxSS_2Choices = [ u"1", u"2", u"3", u"4" ]
		self.m_comboBoxSS_2 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_2Choices, wx.CB_READONLY )
		self.m_comboBoxSS_2.SetSelection( 0 )
		self.m_comboBoxSS_2.Enable( False )
		self.m_comboBoxSS_2.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_2, 1, 0, 5 )
		
		self.m_staticTextSS_4 = wx.StaticText( self, wx.ID_ANY, u"яркость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_4.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_4, 0, wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlSS_1 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSS_1.Enable( False )
		self.m_textCtrlSS_1.SetMaxSize( wx.Size( 80,-1 ) )
		
		bSizer7.Add( self.m_textCtrlSS_1, 0, 0, 5 )
		
		self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )
		bSizer7.Add( self.m_staticText411, 0, wx.ALL, 5 )
		
		
		gSizer21.Add( bSizer7, 1, 0, 0 )
		
		self.m_staticTextSS_5 = wx.StaticText( self, wx.ID_ANY, u"скорость бегущих огней:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_5.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_5, 0, wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlSS_2 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSS_2.Enable( False )
		self.m_textCtrlSS_2.SetMaxSize( wx.Size( 80,-1 ) )
		
		bSizer8.Add( self.m_textCtrlSS_2, 0, 0, 5 )
		
		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )
		bSizer8.Add( self.m_staticText421, 0, wx.ALL, 5 )
		
		
		gSizer21.Add( bSizer8, 1, 0, 0 )
		
		self.m_staticTextSS_6 = wx.StaticText( self, wx.ID_ANY, u"время звукового сигнала:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_6.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_6, 0, wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlSS_3 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSS_3.Enable( False )
		self.m_textCtrlSS_3.SetMaxSize( wx.Size( 80,-1 ) )
		
		bSizer12.Add( self.m_textCtrlSS_3, 0, 0, 5 )
		
		self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, u"мс", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )
		bSizer12.Add( self.m_staticText431, 0, wx.ALL, 5 )
		
		
		gSizer21.Add( bSizer12, 1, 0, 0 )
		
		self.m_staticTextSS_7 = wx.StaticText( self, wx.ID_ANY, u"задержка между звук-ми сигналами:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_7.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_7, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlSS_4 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSS_4.Enable( False )
		self.m_textCtrlSS_4.SetMaxSize( wx.Size( 80,-1 ) )
		
		bSizer13.Add( self.m_textCtrlSS_4, 0, 0, 5 )
		
		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"мс", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		bSizer13.Add( self.m_staticText441, 0, wx.ALL, 5 )
		
		
		gSizer21.Add( bSizer13, 1, 0, 0 )
		
		self.m_staticTextSS_8 = wx.StaticText( self, wx.ID_ANY, u"приоритет входа 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_8.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_8, 0, wx.ALL, 5 )
		
		m_comboBoxSS_3Choices = [ u"1", u"2", u"3" ]
		self.m_comboBoxSS_3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_3Choices, wx.CB_READONLY )
		self.m_comboBoxSS_3.SetSelection( 2 )
		self.m_comboBoxSS_3.Enable( False )
		self.m_comboBoxSS_3.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_3, 0, 0, 5 )
		
		self.m_staticTextSS_9 = wx.StaticText( self, wx.ID_ANY, u"приоритет входа 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_9.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_9, 0, wx.ALL, 5 )
		
		m_comboBoxSS_4Choices = [ u"1", u"2", u"3" ]
		self.m_comboBoxSS_4 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_4Choices, wx.CB_READONLY )
		self.m_comboBoxSS_4.SetSelection( 1 )
		self.m_comboBoxSS_4.Enable( False )
		self.m_comboBoxSS_4.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_4, 0, 0, 5 )
		
		self.m_staticTextSS_10 = wx.StaticText( self, wx.ID_ANY, u"приоритет входа 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_10.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_10, 0, wx.ALL, 5 )
		
		m_comboBoxSS_5Choices = [ u"1", u"2", u"3" ]
		self.m_comboBoxSS_5 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_5Choices, wx.CB_READONLY )
		self.m_comboBoxSS_5.SetSelection( 0 )
		self.m_comboBoxSS_5.Enable( False )
		self.m_comboBoxSS_5.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_5, 0, 0, 5 )
		
		self.m_staticTextSS_11 = wx.StaticText( self, wx.ID_ANY, u"активация входа 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_11.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_11, 0, wx.ALL, 5 )
		
		m_comboBoxSS_6Choices = [ u"0", u"1" ]
		self.m_comboBoxSS_6 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_6Choices, wx.CB_READONLY )
		self.m_comboBoxSS_6.SetSelection( 0 )
		self.m_comboBoxSS_6.Enable( False )
		self.m_comboBoxSS_6.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_6, 0, 0, 5 )
		
		self.m_staticTextSS_12 = wx.StaticText( self, wx.ID_ANY, u"активация входа 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_12.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_12, 0, wx.ALL, 5 )
		
		m_comboBoxSS_7Choices = [ u"0", u"1" ]
		self.m_comboBoxSS_7 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_7Choices, wx.CB_READONLY )
		self.m_comboBoxSS_7.SetSelection( 1 )
		self.m_comboBoxSS_7.Enable( False )
		self.m_comboBoxSS_7.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_7, 0, 0, 5 )
		
		self.m_staticTextSS_13 = wx.StaticText( self, wx.ID_ANY, u"активация входа 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_13.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_13, 0, wx.ALL, 5 )
		
		m_comboBoxSS_8Choices = [ u"0", u"1" ]
		self.m_comboBoxSS_8 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_8Choices, wx.CB_READONLY )
		self.m_comboBoxSS_8.SetSelection( 1 )
		self.m_comboBoxSS_8.Enable( False )
		self.m_comboBoxSS_8.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_8, 0, 0, 5 )
		
		self.m_staticTextSS_14 = wx.StaticText( self, wx.ID_ANY, u"звуковое оповещение входа 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_14.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_14, 0, wx.ALL, 5 )
		
		m_comboBoxSS_9Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_9 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_9Choices, wx.CB_READONLY )
		self.m_comboBoxSS_9.SetSelection( 0 )
		self.m_comboBoxSS_9.Enable( False )
		self.m_comboBoxSS_9.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_9, 0, 0, 5 )
		
		self.m_staticTextSS_15 = wx.StaticText( self, wx.ID_ANY, u"звуковое оповещение входа 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_15.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_15, 0, wx.ALL, 5 )
		
		m_comboBoxSS_10Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_10 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_10Choices, wx.CB_READONLY )
		self.m_comboBoxSS_10.SetSelection( 0 )
		self.m_comboBoxSS_10.Enable( False )
		self.m_comboBoxSS_10.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_10, 0, 0, 5 )
		
		self.m_staticTextSS_16 = wx.StaticText( self, wx.ID_ANY, u"звуковое оповещение входа 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_16.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_16, 0, wx.ALL, 5 )
		
		m_comboBoxSS_11Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_11 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_11Choices, wx.CB_READONLY )
		self.m_comboBoxSS_11.SetSelection( 0 )
		self.m_comboBoxSS_11.Enable( False )
		self.m_comboBoxSS_11.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_11, 0, 0, 5 )
		
		self.m_staticTextSS_17 = wx.StaticText( self, wx.ID_ANY, u"реле подтверждения входа 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_17.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_17, 0, wx.ALL, 5 )
		
		m_comboBoxSS_12Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_12 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_12Choices, wx.CB_READONLY )
		self.m_comboBoxSS_12.SetSelection( 0 )
		self.m_comboBoxSS_12.Enable( False )
		self.m_comboBoxSS_12.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_12, 0, 0, 5 )
		
		self.m_staticTextSS_18 = wx.StaticText( self, wx.ID_ANY, u"реле подтверждения входа 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_18.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_18, 0, wx.ALL, 5 )
		
		m_comboBoxSS_13Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_13 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_13Choices, wx.CB_READONLY )
		self.m_comboBoxSS_13.SetSelection( 1 )
		self.m_comboBoxSS_13.Enable( False )
		self.m_comboBoxSS_13.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_13, 0, 0, 5 )
		
		self.m_staticTextSS_19 = wx.StaticText( self, wx.ID_ANY, u"реле подтверждения входа 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_19.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_19, 0, wx.ALL, 5 )
		
		m_comboBoxSS_14Choices = [ u"нет", u"да" ]
		self.m_comboBoxSS_14 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_14Choices, wx.CB_READONLY )
		self.m_comboBoxSS_14.SetSelection( 0 )
		self.m_comboBoxSS_14.Enable( False )
		self.m_comboBoxSS_14.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_14, 0, 0, 5 )
		
		self.m_staticTextSS_20 = wx.StaticText( self, wx.ID_ANY, u"громкость звукового сигнала:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_20.Wrap( -1 )
		gSizer21.Add( self.m_staticTextSS_20, 0, wx.ALL, 5 )
		
		m_comboBoxSS_15Choices = [ u"МИН", u"МАКС" ]
		self.m_comboBoxSS_15 = wx.ComboBox( self, wx.ID_ANY, u"МИН", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_15Choices, 0 )
		self.m_comboBoxSS_15.SetSelection( 0 )
		self.m_comboBoxSS_15.Enable( False )
		self.m_comboBoxSS_15.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer21.Add( self.m_comboBoxSS_15, 0, 0, 5 )
		
		self.m_buttonSS_1 = wx.Button( self, wx.ID_ANY, u"настройки от производителя", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSS_1.Enable( False )
		
		gSizer21.Add( self.m_buttonSS_1, 0, wx.ALL, 5 )
		
		self.m_buttonSS_2 = wx.Button( self, wx.ID_ANY, u"записать значения в EEPROM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSS_2.Enable( False )
		
		gSizer21.Add( self.m_buttonSS_2, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer21, 0, 0, 2 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer4.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 13, 2, 2, 0 )
		
		gSizer3.SetMinSize( wx.Size( 300,300 ) ) 
		self.m_staticTextMB_1 = wx.StaticText( self, wx.ID_ANY, u"Настройки MODBUS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_1.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_1, 0, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		gSizer3.Add( self.m_staticText381, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_2 = wx.StaticText( self, wx.ID_ANY, u"ID устройства:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_2.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_2, 0, wx.ALL, 5 )
		
		self.m_textCtrlMB_1 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlMB_1.Enable( False )
		self.m_textCtrlMB_1.SetMaxSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_textCtrlMB_1, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_3 = wx.StaticText( self, wx.ID_ANY, u"скорость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_3.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_3, 0, wx.ALL, 5 )
		
		m_comboBoxMB_1Choices = [ u"2400", u"4800", u"9600", u"19200" ]
		self.m_comboBoxMB_1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_1Choices, wx.CB_READONLY )
		self.m_comboBoxMB_1.SetSelection( 0 )
		self.m_comboBoxMB_1.Enable( False )
		self.m_comboBoxMB_1.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_1, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_4 = wx.StaticText( self, wx.ID_ANY, u"стоп-биты", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_4.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_4, 0, wx.ALL, 5 )
		
		m_comboBoxMB_2Choices = [ u"1", u"2", u"1.5" ]
		self.m_comboBoxMB_2 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_2Choices, wx.CB_READONLY )
		self.m_comboBoxMB_2.SetSelection( 2 )
		self.m_comboBoxMB_2.Enable( False )
		self.m_comboBoxMB_2.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_2, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_5 = wx.StaticText( self, wx.ID_ANY, u"четность:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_5.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_5, 0, wx.ALL, 5 )
		
		m_comboBoxMB_3Choices = [ u"нет", u"чет", u"нечет" ]
		self.m_comboBoxMB_3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_3Choices, wx.CB_READONLY )
		self.m_comboBoxMB_3.SetSelection( 0 )
		self.m_comboBoxMB_3.Enable( False )
		self.m_comboBoxMB_3.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_3, 0, wx.ALL, 5 )
		
		self.m_buttonMB_1 = wx.Button( self, wx.ID_ANY, u"настройки от производителя", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMB_1.Enable( False )
		
		gSizer3.Add( self.m_buttonMB_1, 0, wx.ALL, 5 )
		
		self.m_buttonMB_2 = wx.Button( self, wx.ID_ANY, u"записать значения в EEPROM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMB_2.Enable( False )
		
		gSizer3.Add( self.m_buttonMB_2, 0, wx.ALL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline10.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline10, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline11.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline11, 1, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		gSizer3.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_staticTextSN_1 = wx.StaticText( self, wx.ID_ANY, u"серийный номер:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSN_1.Wrap( -1 )
		gSizer3.Add( self.m_staticTextSN_1, 0, wx.ALL, 5 )
		
		self.m_textCtrlSN_1 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSN_1.Enable( False )
		self.m_textCtrlSN_1.SetMaxSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_textCtrlSN_1, 0, wx.ALL, 5 )
		
		self.m_buttonSN_1 = wx.Button( self, wx.ID_ANY, u"прочитать настройки", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSN_1.Enable( False )
		
		gSizer3.Add( self.m_buttonSN_1, 0, wx.ALL, 5 )
		
		self.m_buttonSN_2 = wx.Button( self, wx.ID_ANY, u"записать серийный номер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSN_2.Enable( False )
		
		gSizer3.Add( self.m_buttonSN_2, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		gSizer3.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		gSizer3.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_buttonRST_1 = wx.Button( self, wx.ID_ANY, u"перезагрузить MCU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonRST_1.Enable( False )
		
		gSizer3.Add( self.m_buttonRST_1, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer3, 0, 0, 2 )
		
		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer4.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer4, 1, 0, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Версия программы: 1.0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText49.Wrap( -1 )
		bSizer6.Add( self.m_staticText49, 1, wx.ALL|wx.RIGHT, 5 )
		
		
		bSizer9.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonCOM_1.Bind( wx.EVT_BUTTON, self.PressComButton )
		self.m_textCtrlSS_1.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_textCtrlSS_2.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_textCtrlSS_3.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_textCtrlSS_4.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_comboBoxSS_3.Bind( wx.EVT_COMBOBOX, self.CheckPriority1 )
		self.m_comboBoxSS_4.Bind( wx.EVT_COMBOBOX, self.CheckPriority2 )
		self.m_comboBoxSS_5.Bind( wx.EVT_COMBOBOX, self.CheckPriority3 )
		self.m_buttonSS_1.Bind( wx.EVT_BUTTON, self.SendDefaultWorkSettings )
		self.m_buttonSS_2.Bind( wx.EVT_BUTTON, self.SendWorkSettings )
		self.m_textCtrlMB_1.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_buttonMB_1.Bind( wx.EVT_BUTTON, self.SendModbusDefaultSettings )
		self.m_buttonMB_2.Bind( wx.EVT_BUTTON, self.SendModbusSettings )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.InsertPassword )
		self.m_textCtrlSN_1.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_buttonSN_1.Bind( wx.EVT_BUTTON, self.SendReadAllSettings )
		self.m_buttonSN_2.Bind( wx.EVT_BUTTON, self.SendWriteSerNum )
		self.m_buttonRST_1.Bind( wx.EVT_BUTTON, self.SendResetMcu )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PressComButton( self, event ):
		event.Skip()
	
	def TextCtrlCheckDigit( self, event ):
		event.Skip()
	
	
	
	
	def CheckPriority1( self, event ):
		event.Skip()
	
	def CheckPriority2( self, event ):
		event.Skip()
	
	def CheckPriority3( self, event ):
		event.Skip()
	
	def SendDefaultWorkSettings( self, event ):
		event.Skip()
	
	def SendWorkSettings( self, event ):
		event.Skip()
	
	
	def SendModbusDefaultSettings( self, event ):
		event.Skip()
	
	def SendModbusSettings( self, event ):
		event.Skip()
	
	def InsertPassword( self, event ):
		event.Skip()
	
	
	def SendReadAllSettings( self, event ):
		event.Skip()
	
	def SendWriteSerNum( self, event ):
		event.Skip()
	
	def SendResetMcu( self, event ):
		event.Skip()
	

