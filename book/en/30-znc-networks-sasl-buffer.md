# ZNC: networks, SASL and buffers

Once the client can connect securely to ZNC, add an upstream IRC network.

```text
WeeChat -> ZNC -> IRC network
```

These are two separate connections, and TLS should be considered on both.

When supported by the IRC network, ZNC can authenticate the upstream IRC account using SASL. This is the IRC account, not the credentials used by the local client to log into ZNC.

Use placeholders such as `IRC_ACCOUNT` and `IRC_SECRET` in documentation and keep real secrets out of Git.

ZNC can retain messages for disconnected clients. Buffer size and retention are therefore privacy and operational decisions as well as convenience features.

ZNC also has a module system. Enable only functionality you understand and need; additional components mean additional configuration, state and potential attack surface.
