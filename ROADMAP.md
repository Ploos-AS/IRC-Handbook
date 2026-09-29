# Roadmap

## M0 — Foundation

- repository architecture
- bilingual source layout (NO/EN)
- table of contents
- Pandoc-oriented build entry points
- HTML, EPUB, Kindle-friendly EPUB and PDF targets
- CI smoke build
- licensing and contribution notes

## M1 — IRC fundamentals

- IRC architecture and terminology
- first connection
- essential commands
- channels, modes and etiquette
- accounts, NickServ/ChanServ, TLS and SASL
- modern IRCv3 overview

## M2 — Clients and shell accounts

- desktop, terminal, mobile and web clients
- Irssi and WeeChat labs
- Unix shell fundamentals for IRC users
- SSH keys
- tmux and screen
- persistent sessions
- shell providers vs VPS

## M3 — Bouncers

- bouncer concepts and threat model
- ZNC
- soju
- classic bouncer history
- multi-network and multi-client setups
- TLS, SASL, logs and history

## M4 — Bots

- bot architecture
- Eggdrop
- EnergyMech
- Sopel
- Dancer and other classic bots
- safe operation and permissions
- writing a minimal IRC bot

## M5 — Protocol and IRCv3

- wire protocol
- registration
- PING/PONG
- numerics
- CTCP
- ISUPPORT
- CAP negotiation
- IRCv3 capabilities
- message tags, server-time and history

## M6 — Running infrastructure

- VPS design
- systemd
- containers
- monitoring
- backups
- DNS and TLS
- IRCd and services
- Ergo as a modern integrated IRC server

## M7 — Security, privacy and operations

- IP visibility and what bouncers do/not hide
- SSH hardening
- TLS validation
- SASL and certfp
- secrets handling
- DCC considerations
- logs and retention
- abuse handling and operational hygiene

## M8 — Final lab and publishing

- complete persistent IRC environment
- shell + client + bouncer + bot
- reproducible lab validation
- diagrams and screenshots
- language parity review
- HTML/EPUB/Kindle/PDF release pipeline
- release checklist and first publication candidate
