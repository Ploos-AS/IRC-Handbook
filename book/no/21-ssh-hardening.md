# SSH-hardening uten å låse deg ute

SSH er administrasjonsinngangen til serveren. Endringer bør derfor gjøres kontrollert.

## 1. Få nøkkelinnlogging til å virke først

Fra klientmaskinen oppretter du ved behov et nøkkelpar:

```sh
ssh-keygen -t ed25519
```

Installer den offentlige nøkkelen på serverkontoen og test en **ny, separat SSH-forbindelse** før du endrer autentiseringspolicy.

Ikke lukk den fungerende administrasjonssesjonen før den nye innloggingen er verifisert.

## 2. Stram inn policy etter verifisering

Når nøkkelinnlogging fungerer, kan serverens SSH-policy strammes inn etter behov. Typiske mål er:

- unngå direkte root-innlogging
- redusere eller deaktivere passordinnlogging når nøkkeltilgang er verifisert
- tillate bare nødvendige brukere
- holde OpenSSH oppdatert

Eksakt konfigurasjon avhenger av Debian/OpenSSH-versjonen og hvordan VPS-leverandørens recovery-konsoll fungerer.

## 3. Valider før reload

Etter endringer bør SSH-konfigurasjonen valideres med verktøyene som følger den installerte OpenSSH-versjonen før tjenesten reloades.

Behold en eksisterende sesjon åpen mens du tester en ny.

## Recovery

Før hardening bør du vite hvordan du får konsolltilgang fra VPS-leverandøren dersom SSH blir utilgjengelig.

Sikkerhet som gjør administratoren permanent utestengt er ikke et godt driftsoppsett.
