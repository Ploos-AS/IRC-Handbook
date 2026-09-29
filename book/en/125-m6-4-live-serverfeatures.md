# M6.4: live ServerFeatures

M6.4 closes the gap between being able to parse ISUPPORT and actually following ISUPPORT.

The session receives 005, updates ServerFeatures, uses active CASEMAPPING in message logic, and exposes PREFIX and CHANMODES as structured rules.

This matters for interoperability because IRC networks are not configured identically. The next step is to connect these rules to a live channel model with NAMES replay and dynamic MODE state.
