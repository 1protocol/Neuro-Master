from lava.magma.core.process.process import AbstractProcess
from lava.magma.core.process.variable import Var
from lava.magma.core.process.ports.ports import InPort, OutPort

class ProtocolOneLava(AbstractProcess):
    """Donanım etkileşimi için temel Lava nöron iskeleti"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        shape = kwargs.get("shape", (1,))
        self.s_in = InPort(shape=shape)
        self.a_out = OutPort(shape=shape)
        self.v = Var(shape=shape, init=0)
        self.vth = Var(shape=shape, init=10)
