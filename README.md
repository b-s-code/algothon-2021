# My Algothon 2021 Trading Algorithm

Goals
---

I wrote this algorithm for Algothon 2021 algorithmic trading competition.  The goals of this algorithm are:

* Receive tabular price data where columns represent individual financial instruments and rows represent different days
* Set initial positions once a sufficient number of trading days (enough time to be able to calculate moving averages of required length) have elapsed
* Determine buy/sell signals for by comparing one short term weighted moving average and one long term unweighted moving average for each financial instrument
* Update positions for each financial instrument in response to buy/sell signals

Parameters
---

Parameters of the algorithm include:

* `nInst` - Number of financial instruments under consideration (global variable)
* `k` - Number of days for short term moving average (local to `getMyPosition()`)

	* value is `4` by default

* `l` - Number of days for long term moving average (local to `getMyPosition()`)

	* value is `50` by default

What I Did
---

To create this algorithm, I:

* Interpreted the instructions given in the Algothon 2021 competition
* Examined the code in `eval.py` that would be used to run and evaluate the effectiveness of my algorithm
* Took note of how data was stored in `prices250.txt`
* Researched trading strategies
* Decided to implement a simple moving average crossover trading strategy
* Prototyped a simple implementation of my chosen strategy using a numPy and a single Python script, ignoring how the final program needed to interact with the evaluation program for the competition
* Wrote, tested and tested a program implementing my intended algorithm in a way that could be evaluated by `eval.py`
* Extended the algorithm to use a _weighted_ moving average to track the short term price trends of the different financial instruments
* Tested and evaluated the program again

Notes
---

Original files provided for the competition are in the *competition-files* folder.  `myAlgo.py` contained my code.
