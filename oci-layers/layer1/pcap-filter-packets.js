const pcap = require("pcap");

const INTERFACE_NAME = "eth0";
const TARGET_MAC = "00:11:22:33:44:55";

const pcapSession = pcap.createSession(INTERFACE_NAME, `ether src ${TARGET_MAC}`);

pcapSession.on("packet", (rawPacket) => {
  console.log("Packet captured!");
});

console.log(`Capturing packets on ${INTERFACE_NAME} with MAC ${TARGET_MAC}`);
