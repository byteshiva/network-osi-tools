const dns = require('dns');

const domainName = 'www.google.com';

dns.resolve4(domainName, (err, addresses) => {
    if (err) throw err;

    console.log(`IPv4 addresses for ${domainName}: ${JSON.stringify(addresses)}`);
});

dns.resolve6(domainName, (err, addresses) => {
    if (err) throw err;

    console.log(`IPv6 addresses for ${domainName}: ${JSON.stringify(addresses)}`);
});

dns.resolveCname(domainName, (err, addresses) => {
    if (err) throw err;

    console.log(`CNAME for ${domainName}: ${JSON.stringify(addresses)}`);
});
