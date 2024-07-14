from pyModbusTCP.client import ModbusClient

class ModbusClientClass:
    def __init__(self, host):
        self.host = host
        self.client = ModbusClient(host=self.host, port=502, unit_id=1)
        self.connect_server()

    def connect_server(self):
        if self.client.open():
            print(f"Status: Connected to {self.host} port 502")
        else:
            print(f"Status: Connection Failed")

    def close_connect(self):
        if self.client.open():
            print("Status: Close to connect")
            self.client.close()
        else:
            print("Status: No connected")

    def read_coils(self, coil_bound):
        if self.client.is_open:
            coils = self.client.read_coils(coil_bound[0], coil_bound[1])
            return coils

    def write_coil(self, index, value):
        try:
            self.client.write_single_coil(index, value)
        except Exception as e:
            print(f"Error: {e}")

    def read_regs(self, reg_bound):
        if self.client.is_open:
            regs = self.client.read_holding_registers(reg_bound[0], reg_bound[1])
            return regs

    def write_reg(self, index, value):
        try:
            self.client.write_single_register(index, value)
        except Exception as e:
            print(f"Error: {e}")

# ModbusClientClass("192.168.177.163")
