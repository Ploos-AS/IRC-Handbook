# Fuzzing has boundaries

This harness is deliberately small and uses only the Python standard library. It is not a replacement for a dedicated fuzzer or property-testing framework.

Its value is educational and practical: the mechanism is visible, seeds are stable and tests require no extra dependency. Parse failures for mutations that are no longer valid IRC messages are expected; parseable sequences must not corrupt state.
