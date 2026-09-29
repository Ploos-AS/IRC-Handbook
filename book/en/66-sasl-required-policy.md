# When SASL is required

Supporting SASL and requiring SASL are different policies.

The minimal bot now supports `IRC_SASL_REQUIRED=1`. In this mode the session fails if the server does not advertise SASL, rejects the capability request or authentication fails.

This allows a deployment to state explicitly that it must not continue as an unauthenticated client. Policy remains separate from the underlying CAP/SASL protocol mechanism.
