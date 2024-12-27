# 写一个modbus的客户端
from pymodbus.client import ModbusTcpClient

from pymodbus.datastore import ModbusSlaveContext

def connect_modbus_server(host,port):
    """
    连接modbus服务器
    :param host: 主机地址
    :param port: 端口号
    :return: ModbusTcpClient对象
    """
    master=ModbusTcpClient(host,port=port)
    assert master.connect(),ConnectionError("连接失败")
    return master

def read_coils(master:ModbusTcpClient,address:int,count,slave):
    """
    读取线圈状态
    :param master: ModbusTcpClient对象
    :param address: 起始地址
    :param count: 数量
    :param slave: 从站地址
    :return: 线圈状态列表
    """
    code0x01 = master.read_coils(address=address, count=count, slave=slave)
    return code0x01.bits
def read_discrete_inputs(master,address,count,slave):
    """
    读取离散输入状态
    :param master: ModbusTcpClient对象
    :param address: 起始地址
    :param count: 数量
    :param slave: 从站地址
    :return: 离散输入状态列表
    """
    code0x02 = master.read_discrete_inputs(address=address, count=count, slave=slave)
    return code0x02.bits
def read_holding_registers(master,address,count,slave):
    """
    读取保持寄存器
    :param master: ModbusTcpClient对象
    :param address: 起始地址
    :param count: 数量
    :param slave: 从站地址
    :return: 保持寄存器列表
    """
    code0x03 = master.read_holding_registers(address=address, count=count, slave=slave)
    return code0x03.registers
def read_input_registers(master,address,count,slave):
    """
    读取输入寄存器
    :param master: ModbusTcpClient对象
    :param address: 起始地址
    :param count: 数量
    :param slave: 从站地址
    :return: 输入寄存器列表
    """
    code0x04 = master.read_input_registers(address=address, count=count, slave=slave)
    return code0x04.registers
# 根据传递的错误码打印错误信息
def print_error(error_code):
    """
    根据传递的错误码打印错误信息
    :param error_code: 错误码
    :return: None
    """
    if error_code==0x01:
        print("非法函数")
    elif error_code==0x02:
        print("非法数据地址")
    elif error_code==0x03:
        print("非法数据值")
    elif error_code==0x04:
        print("服务器设备故障")
    elif error_code==0x05:
        print("确认")
    elif error_code==0x06:
        print("从站设备忙")
    elif error_code==0x07:
        print("从站拒绝执行请求")
    elif error_code==0x08:
        print("目标从站不可用")
    elif error_code==0x0A:
        print("网关目标从站不可用")
    elif error_code==0x0B:
        print("网关目标设备响应失败")
