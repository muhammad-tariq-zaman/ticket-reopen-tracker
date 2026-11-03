# ticket-reopen-tracker

Measure which ticket categories keep coming back: reopen rate per category, highest first, with small samples flagged so they are not over-read.

## How to run

```sh
python3 main.py tickets.csv
```

## Example output

```
VPN: 50% reopened (10 tickets)
Printer: 10% reopened (20 tickets)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
