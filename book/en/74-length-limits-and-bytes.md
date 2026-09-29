# Length limits and bytes

Classic IRC is associated with a small 512-byte message limit including line termination. The important unit is bytes, not characters: UTF-8 characters may occupy multiple bytes.

Modern IRC and IRCv3 environments can expose mechanisms or server properties that affect usable message sizes. A client should therefore not translate the historical rule into a simplistic “512 characters”.

Our educational client keeps outgoing messages deliberately small for now; a later serializer can incorporate advertised server properties.
