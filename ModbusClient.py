from pyModbusTCP.client import ModbusClient

class ModbusClientClass:
    def __init__(self, host, coil_bound = [0, 10], reg_bound = [0, 10]):
        self.host = host
        self.coil_bound = coil_bound
        self.coil_bound[1] = self.coil_bound[1]+1
        self.reg_bound = reg_bound
        self.reg_bound[1] = reg_bound[1]+1
        self.client = ModbusClient(host=self.host, port=502, unit_id=1)
        self.connect_server()

    def connect_server(self):
        if self.client.open():
            print(f"Status: Connected to {self.host} port 502")
            self.read_regs()
            self.client.close()
        else:
            print(f"Status: Connection Failed")

    def read_coils(self):
        if self.client.is_open:
            coils = self.client.read_coils(self.coil_bound[0], self.coil_bound[1])
            if coils:
                print("Read Coils:")
                for index in range(self.coil_bound[0], self.coil_bound[1]):
                    print(f"\n{index}: {coils[index]}")

    def write_coil(self, index, value):
        try:
            self.client.write_single_coil(index, bool(value))
        except Exception as e:
            print(f"Error: {e}")

    def read_regs(self):
        if self.client.is_open:
            regs = self.client.read_holding_registers(self.reg_bound[0], self.reg_bound[1])
            if regs:
                print("Read Coils:")
                for index in range(self.reg_bound[0], self.reg_bound[1]):
                    print(f"\n{index}: {regs[index]}")

    def write_reg(self, index, value):
        try:
            self.client.write_single_register(index, value)
        except Exception as e:
            print(f"Error: {e}")

ModbusClientClass("192.168.177.163")
