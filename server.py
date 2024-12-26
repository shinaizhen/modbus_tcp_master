from pymodbus.server import StartTcpServer

from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext,
)

datablock=ModbusSequentialDataBlock.create()
context=ModbusSlaveContext(
    di=datablock,
    co=datablock,
    hr=datablock,
    ir=datablock,
)
signal=True

store=ModbusServerContext(slaves=context, single=signal)

if __name__=="__main__":
    address=("localhost",503)
    StartTcpServer(
        context=store,
        address=address,
    )