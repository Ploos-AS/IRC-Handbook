# Testing CAP and SASL in CI

The fake IRC server now has a dedicated SASL scenario that verifies CAP LS, CAP REQ, ACK, AUTHENTICATE PLAIN, the test payload, numeric 903, CAP END, numeric 001 and JOIN.

The account `acct` and value `secret` are synthetic test data and are never used against an external service.

GitHub Actions runs the unit and integration suite without connecting to public IRC and without repository secrets, across multiple Python versions.
