const os = require("os");

const interfaces = os.networkInterfaces();

console.log("Network interfaces:");

for (const interfaceName in interfaces) {
  console.log(`${interfaceName}:`);
  for (const { address, netmask, family } of interfaces[interfaceName]) {
    console.log(`  ${family} ${address}/${netmask}`);
  }
}
