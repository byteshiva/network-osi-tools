const net = require('net');

const PORT = 3000;
const ENCODING = 'utf8';

const server = net.createServer((socket) => {
  socket.on('data', (data) => {
    // apply presentation layer function
    const transformedData = presentationLayerFunction(data.toString(ENCODING));

    // send the transformed data to the application layer
    socket.write(transformedData);
  });
});

server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

function presentationLayerFunction(data) {
  // example function that adds a prefix to the data
  return `[PREFIX] ${data}`;
}
