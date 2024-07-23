#в этом файле все константы
magic_word = 'SIU_LED_V2_START_PROGRAMMING'
password_to_change_serial = 'иди нахуй'

#номера команд от ПК
COMMAND_CONNECTION = 0x19
COMMAND_READ_ALL_SETTINGS = 0x28
COMMAND_WRITE_WORK_SETTINGS = 0x37
COMMAND_WRITE_UART_SETTINGS = 0x46
COMMAND_WRITE_SERIAL_NUMBER = 0x55
COMMAND_RESET_MCU = 0x91

COMMAND_CONNECTION_NEG = 0xE6
COMMAND_READ_ALL_SETTINGS_NEG = 0xD7
COMMAND_WRITE_WORK_SETTINGS_NEG = 0xC8
COMMAND_WRITE_UART_SETTINGS_NEG = 0xB9
COMMAND_WRITE_SERIAL_NUMBER_NEG = 0xAA
COMMAND_RESET_MCU_NEG = 0x6E

#индексы буфера
INDEX_COMMAND = 0
INDEX_COMMAND_NEG = 1
INDEX_SERIALNUMBER_H = 2
INDEX_SERIALNUMBER_L = 3

#возможные скорости юарта
SPEED_LIST = [9600, 19200, 4800, 2400]
PARITY_LIST = ['N', 'E', 'O']
STOPBITS_LIST = [1, 1.5, 2]

#settings_default
DEFAULT_CONTROL_SOURCE = 0   #источник управления 0-входы, 1-модбас, 2-смешанный
DEFAULT_LED_WORK_COUNT = 4       #количество бегущих огней от 1 до 4
DEFAULT_BRIGHTNESS = 100     #яркость от 0 до 100%
DEFAULT_LED_SPEED = 70     #скорость бегущих огней от 0 до 100%
DEFAULT_BUZZER_ON_TIME = 500    #время писка излучателя от 200 до 2000мс
DEFAULT_BUZZER_OFF_TIME = 500    #время паузы излучателя от 200 до 2000мс
DEFAULT_PRIORITY_INPUT1 = 3       #приоритет входа от 1 до 3
DEFAULT_PRIORITY_INPUT2 = 2       #приоритет входа от 1 до 3
DEFAULT_PRIORITY_INPUT3 = 1       #приоритет входа от 1 до 3
DEFAULT_INVERT_INPUT1 = 0       #инверсия входа 1 - нет инверсии 0 - есть инверсия
DEFAULT_INVERT_INPUT2 = 1       #инверсия входа 1 - нет инверсии 0 - есть инверсия
DEFAULT_INVERT_INPUT3 = 1       #инверсия входа 1 - нет инверсии 0 - есть инверсия
DEFAULT_INPUT1_BUZ = 0       #писк при срабатывании входа 1
DEFAULT_INPUT2_BUZ = 0       #писк при срабатывании входа 2
DEFAULT_INPUT3_BUZ = 0       #писк при срабатывании входа 3
DEFAULT_INPUT1_RELAY = 0       #реле подтверждения при срабатывании входа 1
DEFAULT_INPUT2_RELAY = 0       #реле подтверждения при срабатывании входа 2
DEFAULT_INPUT3_RELAY = 0       #реле подтверждения при срабатывании входа 3
DEFAULT_WORK_MODE_REG = 10      # текущий режим
DEFAULT_VOLUME = 1      # текущий уровень громкости

#min and max settings
CONTROL_SOURCE_MAX_VALUE = 2      # /*источник управления 0-входы, 1-модбас, 2-смешанный*/
CONTROL_SOURCE_MIN_VALUE = 0
LED_WORK_COUNT_MAX_VALUE = 4       #/*количество бегущих огней от 1 до 4*/
LED_WORK_COUNT_MIN_VALUE = 1
BRIGHTNESS_MAX_VALUE = 100     #/*яркость от 0 до 100%*/
BRIGHTNESS_MIN_VALUE = 0
LED_SPEED_MAX_VALUE = 100     #/*скорость бегущих огней от 0 до 100%*/
LED_SPEED_MIN_VALUE = 0
BUZZER_ON_TIME_MAX_VALUE = 2000    #/*время писка излучателя от 200 до 2000мс */
BUZZER_ON_TIME_MIN_VALUE = 200
BUZZER_OFF_TIME_MAX_VALUE = 2000    #/*время паузы излучателя от 200 до 2000мс */
BUZZER_OFF_TIME_MIN_VALUE = 200
PRIORITY_INPUT_MAX_VALUE = 3       #/*приоритет входа от 1 до 3*/
PRIORITY_INPUT_MIN_VALUE = 1
INVERT_INPUT_MAX_VALUE = 1       #/*инверсия входа 0 - нет инверсии 1 - есть инверсия*/
INVERT_INPUT_MIN_VALUE = 0
INPUT_BUZ_MAX_VALUE = 1       #/*пищалка входа 0 - нет писка 1 - есть писк*/
INPUT_BUZ_MIN_VALUE = 0
INPUT_RELAY_MAX_VALUE = 1       #/*реле подтверждения входа 0 - нет подтверждения 1 - есть подтверждения*/
INPUT_RELAY_MIN_VALUE = 0
WORK_MODE_REG_MAX_VALUE = 13       #/*текущий режим 10-Normoal mode, 11-Red mode, 12-yellow mode, 13-green mode, 14-prestart mode, 15-settnig mode. Если источник управления входы, то нельхя редактировать.*/
WORK_MODE_REG_MIN_VALUE = 10
WORK_VOLUME_MAX_VALUE = 1
WORK_VOLUME_MIN_VALUE = 0

OWN_ID_MAX_VALUE = 255
OWN_ID_MIN_VALUE = 0
SERIAL_NUM_MAX_VALUE = 9999
SERIAL_NUM_MIN_VALUE = 0

#default UART settings
DEFAULT_UART_OWN_ID = 1  #id устройства MODBUS
DEFAULT_UART_SPEED = 9600   #baudrate
DEFAULT_UART_PARITY = 0x04  # 0x00 - none; 0x04 - even; 0x06 - odd
DEFAULT_UART_STOPBITS = 0x00    # 0x00 - 1; 0x20 - 2; 0x30 - 1.5

#онстанты для бутлоадера
MAX_BIN_SYMBOLS = 28671      # максимальное количество символов в прошивке
BYTES_PER_PAGE = 128
MAIN_APP_OFFSET = 0
ACK = 0x79
NACK = 0x1F
BOOTLOADER_KEY_VALUE = [0xAA, 0xAA, 0x55, 0x55]
N_COMMAND = 0   # команда
NEG_N_COMMAND = 1   # команда
N_PAGE = 2  # номер страницы для записи
SIZE_MES = 3  # колчисетво байт далее
FIRST_BYTE_IN_MES = 3  # колчисетво байт далее
RM_Command = 0x11           # read memory
GO_Command = 0x21           # GO command
WM_Command = 0x31           # write memory
RESET_Command = 0x3A        # reset mcu
RESET_KEY_Command = 0xAB    # reset key word in mcu
SET_KEY_Command = 0xBB      # set key word in mcu

#настройки порта бутлоардера
BTL_PORT_SPEED = 19200
BTL_PORT_PARITY = 'E'
BTL_PORT_STOPBITS = 1
