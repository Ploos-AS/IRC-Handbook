# AUTHENTICATE in 400-character chunks

SASL data carried by IRC AUTHENTICATE must be divided into chunks no larger than 400 characters.

`sasl_authenticate_lines()` performs that split. If the encoded payload ends exactly on a 400-character boundary, an additional `AUTHENTICATE +` terminator is emitted. This is the kind of protocol edge case that short test passwords rarely reveal.
