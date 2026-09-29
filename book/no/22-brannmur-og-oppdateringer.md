# Brannmur og oppdateringer

En IRC-shell trenger normalt svært få innkommende tjenester.

## Minimer angrepsflaten

I første fase trenger serveren i hovedsak SSH inn. IRC-klienten oppretter selv utgående forbindelser til IRC-nettverk.

Det betyr at vi ikke trenger å åpne tilfeldige IRC-porter inn til serveren bare fordi vi bruker IRC.

Senere vil en bouncer kreve en egen innkommende lytter. Den åpner vi først når bounceren faktisk installeres.

## Brannmur

Velg én tydelig administrert brannmurløsning og dokumenter reglene. Prinsippet er:

```text
innkommende:
  SSH        tillatt fra ønsket policy
  annet      ikke eksponert uten behov

utgående:
  nødvendige klientforbindelser
```

VPS-leverandørens nettverksbrannmur kan brukes som et ekstra lag, men erstatter ikke forståelsen av hva verten selv lytter på.

## Oppdateringer

Installer sikkerhetsoppdateringer regelmessig. Automatiske sikkerhetsoppdateringer kan være hensiktsmessige, men serveren må fortsatt overvåkes og kunne håndtere nødvendige omstarter.

Før større oppgraderinger:

1. ha fungerende backup
2. kjenn recovery-metoden
3. kontroller ledig diskplass
4. les relevante release notes

En IRC-shell skal være kjedelig å drifte. Stabilitet er en funksjon.
