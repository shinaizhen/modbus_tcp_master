# 写一个modbus的客户端
from pymodbus.client import ModbusTcpClient

from pymodbus.datastore import ModbusSlaveContext

master=ModbusTcpClient("localhost",port=502)

assert master.connect(),ConnectionError("连接失败")

store=ModbusSlaveContext(
    di=[0,1,1,0,0],
    co=[],
    hr=[],
    ir=[],
)

master.write_coils(address=0,values=[1,0,0,1,0],slave=1)
master.write_registers(address=0,values=[500,600,400,100],slave=1)

try:
    code0x01 = master.read_coils(address=0, count=5, slave=1)
    print(code0x01.bits)
    code0x02 = master.read_discrete_inputs(address=0, count=1, slave=1)
    print(code0x02.bits)
    code0x03 = master.read_holding_registers(address=0, count=5, slave=1)
    print(code0x03.registers)
    code0x04 = master.read_input_registers(address=0, count=5, slave=1)
    print(code0x04.registers)
except Exception as e:
    print(e)