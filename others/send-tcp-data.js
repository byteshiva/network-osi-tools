const net = require('net');

const client = new net.Socket();
client.connect(80, 'remote-host', () => {
    console.log('Connected');
    client.write('Hello, World!');
});

client.on('data', (data) => {
    console.log(`Received: ${data}`);
    client.destroy();
});

client.on('close', () => {
    console.log('Connection closed');
});
