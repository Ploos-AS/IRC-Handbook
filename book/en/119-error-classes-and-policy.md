# Error classes and policy

AuthenticationError represents a policy failure and terminates when authentication is mandatory. ServerError, ConnectionClosed, socket failures and TLS failures can flow through reconnect and backoff. Local shutdown returns an explicit stopped result and does not reconnect.

Classification keeps the main loop from guessing failure causes from human-readable text.
