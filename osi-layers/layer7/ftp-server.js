const ftp = require('ftp');
const fs = require('fs');

const ftpClient = new ftp();

const ftpConfig = {
    host: 'ftp.example.com',
    user: 'username',
    password: 'password'
};

ftpClient.connect(ftpConfig);

ftpClient.on('ready', () => {
    ftpClient.list((err, list) => {
        if (err) throw err;
        console.log(list);
    });

    ftpClient.get('remote/path/to/file.txt', (err, stream) => {
        if (err) throw err;
        stream.once('close', () => { ftpClient.end(); });
        stream.pipe(fs.createWriteStream('local/path/to/file.txt'));
    });
});
