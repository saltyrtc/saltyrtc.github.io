Title: Getting Started
Date: 2016-12-03 19:00
Modified: 2016-12-03 19:00
Sort-Order: 2
Summary: Getting started to use SaltyRTC as your signalling service.

# Server

If you want to try out SaltyRTC without much of a hassle, you can use our public server which is available at `wss://server.saltyrtc.org:9287`. **Do not use this server for production!** We may decide to change the port, shut down the server, etc. Our server's public permanent key is `f77fe623b6977d470ac8c7bf7011c4ad08a1d126896795db9d2b4b7a49ae1045` (hex-encoded).

The following sub-sections describe how to set up a self-hosted SaltyRTC server.

## Installation

Install your own self-hosted server by following the instructions of the [SaltyRTC Server for Python][server-installation].

## Configuration

### Permanent Key

We highly recommend to generate a permanent key for the server.

```bash
saltyrtc-server generate <path-for-new-permanent-key>
```

The output contains the hex-encoded public permanent key which needs to be distributed to the clients.

```
Public permanent key: 76bfbb87b72f39ce88db3c7c1780eb3c7cdec5ab07649c9e807f6d2f8b88ca39
```

### TLS Certificate & Key

Although the SaltyRTC protocol is secure without TLS, we still recommend to supply a valid certificate for TLS. Generate it for your domain you want to use the server on. However, it's perfectly fine to not use a certificate during development on a local machine.

The server can be restarted by sending a `HUP` signal to it after a new certificate has been generated (for example by Let's Encrypt's `certbot`).

## Usage

Start the server by running the following command:

```bash
saltyrtc-server -v7 -c serve -sc <tls-certificate> -sk <tls-private-key> <saltyrtc-permanent-key>
```

The arguments `-v` and `-c` control the logging verbosity and style. Run `saltyrtc-server --help` and `saltyrtc-server serve --help` for details on arguments.

# Client

TODO

[server-installation]: https://github.com/saltyrtc/saltyrtc-server-python/blob/master/README.rst#saltyrtc-signalling-server

