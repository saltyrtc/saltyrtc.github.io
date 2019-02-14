Title: Getting Started
Date: 2016-12-03 19:00
Modified: 2016-12-03 19:00
Sort-Order: 2
Summary: Getting started to use SaltyRTC as your signalling service.

# Demo

If you just want to see a demo, you can try out our
[Demo Application][demo-application].

# Server

If you want to try out SaltyRTC without much of a hassle, you can use our 
public server which is available at `wss://server.saltyrtc.org:443`. **Do not 
use this server for production!** We may decide to change the port, shut down 
the server, etc. Our server's public permanent key is 
`f77fe623b6977d470ac8c7bf7011c4ad08a1d126896795db9d2b4b7a49ae1045` 
(hex-encoded).

The following sub-sections describe how to set up the SaltyRTC server for 
Python.

## Installation

Install your own self-hosted server by following the instructions of the 
[SaltyRTC Server for Python Readme][server-installation].

## Configuration

### Permanent Key

We highly recommend to generate a permanent key for the server.

```bash
saltyrtc-server generate <path-for-new-permanent-key>
```

The output contains the hex-encoded public permanent key which needs to be 
distributed to the clients.

### TLS Certificate & Key

Although the SaltyRTC protocol is secure without TLS, we still recommend to 
supply a valid certificate for TLS as it helps to protect metadata. Generate it 
for your domain you want to use the server on.

The server can be restarted by sending a `HUP` signal to it after a new 
certificate has been generated (for example by Let's Encrypt's `certbot`).

During development, it's perfectly fine to omit the certificate.

## Usage

Start the server by running the following command:

```bash
saltyrtc-server -v7 -c serve -sc <tls-certificate> -sk <tls-private-key> -k <saltyrtc-permanent-key>
```

The options `-v` and `-c` control the logging verbosity and format. Use the 
`--help` flag for details on options.

# Client

For this example, we'll explain how to embed the SaltyRTC JavaScript Client 
implementation in your JavaScript application.

## Installation

Follow the instructions of the
[SaltyRTC JavaScript Client Readme][client-installation].

## Usage

To embed SaltyRTC's signalling in your application, you'll need to follow the 
[usage instructions][client-usage] of the JavaScript client.

Set host and port according to the server you want to use. In addition, enable 
the tasks you want to execute (for example initiating a WebRTC peer-to-peer 
connection).

Don't forget that you'll need to exchange the *authentication token* from one 
client to another. We recommend using QR codes for mobile applications.

[server-installation]: https://github.com/saltyrtc/saltyrtc-server-python/blob/master/README.rst#saltyrtc-signalling-server
[demo-application]: https://github.com/saltyrtc/saltyrtc-demo
[client-installation]: https://github.com/saltyrtc/saltyrtc-client-js#installing
[client-usage]: https://github.com/saltyrtc/saltyrtc-client-js#usage

