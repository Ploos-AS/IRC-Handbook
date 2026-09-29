# MODE as actual state

MODE parser output now changes local channel state. Membership modes are stored per member, list modes such as bans are sets of values, modes such as key and limit retain values, and parameter-free modes are simple flags.

Parsing answers what the protocol message means; the state layer answers how the current model changes.
