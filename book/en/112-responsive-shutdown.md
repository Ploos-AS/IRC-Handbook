# Responsive shutdown

The receive loop checks the stop flag between short waits. SIGINT or SIGTERM can therefore stop a completely quiet IRC session without waiting for another server message.

The timeout is a control mechanism rather than a reconnect trigger.
