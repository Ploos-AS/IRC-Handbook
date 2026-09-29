# Channel state as a separate model

An IRC client observes an event stream. To display what a channel looks like now, it must construct local state.

The example client therefore has a `ChannelState` model for members, membership modes, channel modes, valued modes and list modes. Parsing remains separate: first parse a protocol message, then apply its event to state. This makes the model replayable and testable.
