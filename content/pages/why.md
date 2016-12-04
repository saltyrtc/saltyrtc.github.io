Title: Why SaltyRTC?
Date: 2016-12-03 19:00
Modified: 2016-12-03 19:00
Sort-Order: 1
Summary: What is SaltyRTC all about and why should I use it?

# Short

Here's why you should use SaltyRTC. With SaltyRTC,

* signalling data is fully end-to-end encrypted,
* zero trust towards the server is needed,
* no data is stored on the server,
* servers can be self-hosted,
* it doesn't fall apart without SSL/TLS, and
* it's not limited to WebRTC and ORTC.

# Long

We'll take WebRTC signalling solutions as an example to describe existing
signalling solutions and their security issues.

Most existing applications that utilise WebRTC claim that their users are fully 
end-to-end encrypted because WebRTC provides end-to-end encryption. However, 
this is not true. Because if the signalling is not end-to-end encrypted, it's
not guaranteed that the peer you connect to is actually the peer you originally
wanted to establish the connection with. A man-in-the-middle attack is still
very possible. Thus, signalling information authentication and integrity is the
weakest link of WebRTC's end-to-end encryption claim.

But the man-in-the-middle attack isn't the only problem. WebRTC's signalling 
data also contains information about the peer's IP addresses which may leak 
information about its location. It possibly contains information that can be 
used to conclude browser vendor and version, codecs which may lead to installed 
libraries and their versions, etc. Thus, we do not want anyone else but the
other peer we want to communicate with to have access to this data. This can
only be achieved by using end-to-end encryption techniques.

Now that we know why it's important to end-to-end encrypt the signalling 
messages, we'll go through existing signalling solutions and their problems.

## Transport Encryption Solutions

There are lots of available hosted signalling solutions for WebRTC. 
Most of them provide transport encryption and thus require the end user of the 
WebRTC application to trust a third party that relays signalling messages from 
one peer to another before they can communicate directly. For example, 
[Firebase][firebase] offers such a solution. You will have to trust that they 
have no security issues regarding their SSL/TLS settings and certificates. 
Furthermore, providers such as Firebase have full access to the exchanged 
signalling messages in plaintext and are technically able to modify them. While 
you may choose to trust Firebase to not modify or use signalling data in any 
way, they still have obligations to follow national laws and might be compelled 
to hand out the end user's signalling data.

## Self-Hosted Transport Encryption Solutions

There are also plenty of transport encrypted signalling solutions that can be
hosted on your own server, such as [PeerJS][peer-js]. Although this is a better
solution than trusting a third party, the end user still has to trust you to not
modify signalling messages and not have any security issues on your severs.
Even though we usually don't want to admit it, secretly we all know that
certificate and private key handling isn't easy. Moreover, you're also obliged
to follow national laws and might be compelled to hand out your user's
signalling data. So, this is not ideal either.

## SaltyRTC - An End-to-End Encrypted Solution

So, to summarise, we want a signalling solution where the server does not need
to be trusted at all and the messages are end-to-end encrypted. This is exactly
where SaltyRTC comes in. The only thing a SaltyRTC server effectively knows is
what path you're on, whether you are an *initiator* or a *responder* and who
sends which messages to which peer. Because SaltyRTC clients authenticate one
another, the server cannot do any other attack but a denial of service. You can
host your own SaltyRTC server and the protocol is secure even without SSL/TLS.
Even if the (optional) SaltyRTC server permanent key has been compromised,
client-to-client messages are still secure because they're end-to-end encrypted. Furthermore, while SaltyRTC is a simple protocol it is not limited to WebRTC and
ORTC as it can be extended to be used for any signalling purpose desired.

Convinced? [Get started][getting-started] now!

Not convinced, yet? Take a look at
[A Study of WebRTC Security][webrtc-security].

[firebase]: https://firebase.google.com
[peer-js]: https://github.com/peers/peerjs-server
[getting-started]: {filename}/pages/getting_started.md
[webrtc-security]: https://webrtc-security.github.io

