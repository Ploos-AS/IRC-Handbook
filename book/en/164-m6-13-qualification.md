# M6.13 qualification

M6.13 qualifies the explicit registration state machine.

The qualified code commit is:

`00c0cee6e43ca47760d262520f21b28bf0811390`

GitHub Actions run `36628500155` executed the Minimal IRC bot tests on Python 3.11, 3.12, and 3.13. All three jobs passed. Build run `36628500156` also passed.

Qualification covers explicit registration phases, the CAP/SASL sequence, required-SASL failure, nickname collision, one-shot JOIN after 001, and protection against registration events arriving in the wrong phase.

M6.13 also exposed an important CI lesson. During development, some rapid file updates ended up in different commit trees, allowing CI to exercise older test content than intended. The final candidate was therefore constructed atomically from the current main tree using an explicitly verified test blob, one new tree, and one fast-forward commit.

The qualification record is stored in `docs/qualification/M6.13.md`. Later documentation commits do not change which code commit is qualified.