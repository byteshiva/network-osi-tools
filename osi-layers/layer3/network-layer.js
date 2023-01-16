const net = require('net');

const PORT = 3000;

const server = net.createServer((socket) => {
  console.log('New connection');

  socket.on('data', (data) => {
    console.log(`Received: ${data.toString()}`);
    // Send the data back to the client
    socket.write(data);
  });

  socket.on('end', () => {
    console.log('Connection closed');
  });
});

server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
