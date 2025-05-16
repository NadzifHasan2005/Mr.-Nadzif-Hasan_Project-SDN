from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

class SimpleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [0x04]  # OpenFlow 1.3

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        # Tambahkan logika forwarding sederhana di sini
        pass
