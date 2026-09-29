# ZNC on Debian

We now build our first dedicated bouncer.

On Debian, ZNC can be installed from distribution packages:

```sh
sudo apt update
sudo apt install znc
```

Check the version and security updates provided by the Debian release you actually operate.

Do not run the bouncer as root. Use an unprivileged service identity.

A useful deployment sequence is: install ZNC, create configuration, verify the process, test client access in a controlled environment, configure TLS, expose only the required listener, and finally test externally.

Do not open arbitrary firewall ports before you know exactly which authenticated service will listen on them. Keep real ZNC and IRC passwords out of the book repository.
