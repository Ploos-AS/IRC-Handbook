# Eggdrop in practice

Eggdrop is a natural first practical bot because it connects modern operations with classic IRC shell culture.

Use a maintained package or appropriate official project source, and verify the version, documentation and security status before production use. Do not copy an arbitrary old configuration from the Internet and assume it matches the current release.

Run the bot under an unprivileged identity. Protect configuration containing secrets from other local users.

Think about configuration in functional blocks: bot identity, IRC network, TLS, account/SASL, channels, users/permissions, scripts/modules and logging. Exact directives depend on the installed version.

The first milestone is deliberately small: start cleanly, connect securely to a test network, use the expected identity, join one test channel and perform one harmless test function.
