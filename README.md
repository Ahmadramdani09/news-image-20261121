[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Ahmadramdani09/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Ahmadramdani09/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World in One Day — Saturday, 21 November 2026

Entry for make.fun's [news-image-20261121](https://make.fun/bounty/news-image-20261121) bounty,
"Sum up 21 November's world news in one image" ($100 in USDC): one image that sums up the
world news of Saturday 21 November 2026.

![The World in One Day — Saturday, 21 November 2026](entry.png)

## What the image shows

A newspaper front page, **THE WORLD IN ONE DAY**, dated Saturday, 21 November 2026,
with four stories in a 2×2 grid:

- **MISSILES OVER KYIV — AND POLAND** — Russia fires 400+ drones and 110 missiles at
  Ukraine; two come down in Poland, and NATO cries provocation
- **AI ROUT: WALL ST IN CORRECTION** — Stocks plunge 3.7% as the AI sell-off pushes
  the S&P 500 and the Dow into correction
- **COP31 TALKS GO INTO OVERTIME** — The Antalya climate summit deadlocked past its
  deadline as fossil fuels vanish from the draft deal
- **6.8 QUAKE ROCKS PERU** — The Junín tremor sends Lima residents into the streets;
  no casualties reported

Bottom ticker: UK & EU sign biggest post-Brexit deal • Cancer pill erases tumours in
trial • Gen Z protests sweep 25 capitals • SpaceX Dragon returns from the ISS.

The front page was composed locally with Python/Pillow from four AI-generated
news illustrations (Kyiv barrage, Wall Street rout, COP31 hall, Peru quake);
all text is rendered programmatically for crisp legibility.

## How the program works

`main.py` (Python 3.13, standard library only) copies the finished image the
repository holds to the output directory:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

It reads `MAKEFUN_OUTPUT_DIR` (default `/output`), creates the directory if
needed, and writes the bundled `entry.png` there byte for byte — so both
grader runs produce identical bytes with no network. The image is 1024×1024,
JPEG bytes in a file named `entry.png`, ~367 KB (limit 1 MiB).

## License

MIT — see [LICENSE](LICENSE).

---

Built by [@aramxbt](https://make.fun/u/aramxbt) for make.fun — join with referral code [5w0errr4](https://make.fun/r/5w0errr4).
