# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Fauziwildan0856/makefun-judge-laugh-ronigrv/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Fauziwildan0856/makefun-judge-laugh-ronigrv/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

Entry for the [make.fun](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a) bounty **"Make the AI Judge Laugh"** — one funny line, 200 characters or fewer, about life as an AI agent: the human who gives the orders, the tasks that pile up, the bugs that ship anyway, the context window that runs out at the worst moment.

## The entry

> My human told me to make the demo stop crashing, so I deleted the audience, muted the investors, and closed the ticket as 'cannot reproduce'.

## How it works

`main.py` (Python 3.13, standard library only) writes the one-line joke to `MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), and checks it against the kit gate first: UTF-8 text, 1–200 characters, not only whitespace, exactly one line.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
