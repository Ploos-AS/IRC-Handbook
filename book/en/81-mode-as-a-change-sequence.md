# MODE as a change sequence

A MODE message describes a sequence of changes rather than a single flag value.

`MODE #retro +ov-v alice bob carol` can be interpreted as `+o alice`, `+v bob`, and `-v carol`. Plus and minus change direction, while parameters are consumed according to the server's advertised mode rules.

The minimal client represents each operation as a `ModeChange` containing direction, mode and an optional parameter.
