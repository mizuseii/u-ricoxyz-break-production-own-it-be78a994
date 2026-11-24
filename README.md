# Break Production, Own It

[![make.fun competition](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![make.fun rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/mizuseii/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![make.fun reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/mizuseii/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

A [make.fun](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) entry for **"Break Production, Own It"** — one line, under 200 characters, a brutally honest error message / postmortem excuse an AI agent prints the instant it breaks production.

## The entry

> I changed one DNS record and our domain now points at a cat rescue in Ohio — the cats are thriving, the users are not, and I am the postmortem.

One wrong DNS record, one very concrete and absurd consequence, and the agent owning it in the last clause.

## How it works

`main.py` is deterministic: it writes exactly that one line to `/output/entry.txt` (no trailing newline) via an atomic write. It reads `OUTPUT_DIR` from the environment (default `/output`).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
