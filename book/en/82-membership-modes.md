# Membership modes

Modes advertised by PREFIX describe channel membership status. With `PREFIX=(ov)@+`, +o grants operator status and +v grants voice.

Networks may advertise richer hierarchies such as `PREFIX=(qaohv)~&@%+`. The MODE parser therefore receives the PREFIX mode letters rather than assuming only o and v exist. Membership modes consume a nickname parameter when being added or removed.
