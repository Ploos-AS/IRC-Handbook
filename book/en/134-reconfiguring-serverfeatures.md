# Reconfiguring server features

When new 005 data arrives, the registry reconfigures existing channel models with the current CASEMAPPING, PREFIX and CHANMODES.

It also rebuilds the channel index under the active casemapping. This keeps protocol rules centralized in `ServerFeatures` rather than allowing each channel to develop an independent copy of server configuration.
