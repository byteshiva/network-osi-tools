const net = require('net');

const server = net.createServer((socket) => {
    console.log('Client connected');
    socket.on('data', (data) => {
        console.log(`Received: ${data}`);
        socket.write(`Echo: ${data}`);
    });
    socket.on('end', () => {
        console.log('Client disconnected');
    });
});

server.listen(8000, () => {
    console.log('Server started on port 8000');
});
