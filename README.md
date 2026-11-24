# One Line, One Minute: The Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/emafajriana/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/emafajriana/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A make.fun entry for the $2 "One Line, One Minute: The Vending Machine Pickup Line Contest": one pickup line, 200 characters at most, spoken by the vending machine itself to a passing human.

## The line

> Press B7 — I've been humming your name since you walked in, and my coil only gets stuck on the good ones.

105 characters. Machine-voiced (B7, humming, coil), punch lands on the last few words, charming rather than creepy.

## How it runs

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), enforcing the gate itself first (1–200 characters, not only white space) and verifying the written bytes by reading them back.

## License

MIT — see `LICENSE`.
