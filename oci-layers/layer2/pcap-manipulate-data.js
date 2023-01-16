const pcap = require("pcap");

const INTERFACE_NAME = "eth0";

const pcapSession = pcap.createSession(INTERFACE_NAME, "arp");

pcapSession.on("packet", (rawPacket) => {
  const packet = pcap.decode.packet(rawPacket);

  console.log(`Source MAC: ${packet.link.sha}`);
  console.log(`Destination MAC: ${packet.link.dha}`);
});

console.log(`Capturing packets on ${INTERFACE_NAME}`);
