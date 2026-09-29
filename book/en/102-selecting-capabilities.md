# Selecting capabilities

The client has a small desired set: server-time, account-tag and message-tags. SASL is added when credentials are configured.

This wish list is not an assumption about the server. After the complete CAP LS advertisement, the client computes the intersection of desired and available capabilities and requests only that intersection.
