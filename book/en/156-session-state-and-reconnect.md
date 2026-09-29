# 156. Session state and reconnect

An IRC client must distinguish persistent configuration from state that belongs to only one connection.

The server's ISUPPORT values, current nick, channel members and channel modes belong to the active IRC session. When the TCP connection disappears, that knowledge is no longer authoritative.

The example bot therefore collects this information in `SessionState`. Every reconnect creates a new instance. Configuration may persist, but server and channel state starts again.

This prevents members, channel modes or server properties from an old connection from being treated as truth after reconnect.
