# ZNC and soju compared

ZNC and soju address overlapping problems but come from different histories and designs.

| Topic | ZNC | soju |
|---|---|---|
| Core role | IRC bouncer | IRC bouncer |
| Design context | established classic/modular bouncer | modern IRCv3-oriented bouncer |
| Extensions | extensive module concept | stronger focus on protocol and bouncer state |
| Multiple networks | yes | yes |
| Multiple clients | supported; experience depends on client/protocol | central modern use case |
| History | buffer/playback features | modern history/state model |
| IRCv3 | support depends on feature and version | central design concern |

This is an architectural comparison, not a ranking.

Evaluate the actual deployment requirements: client mix, simultaneous devices, required IRCv3 features, history retention, user administration, backup, upgrades and extension needs. Test those requirements against the specific software version you intend to operate.

A bouncer is infrastructure. Choose and operate it according to architecture, security and client experience rather than product name alone.
