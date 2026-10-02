# rule-lattice

Render one-dimensional cellular automata as plain-text patterns. Choose a Wolfram rule, width, number of generations, and optionally a reproducible random starting row.

## Use

Requires Python 3.10+; no packages to install.

```sh
python rule_lattice.py
python rule_lattice.py --rule 90 --width 81 --rows 41
python rule_lattice.py --rule 110 --seed 42 --wrap
```

The default starts with one live cell at the center; `--seed` replaces it with a deterministic random row. Edges behave as zero-valued cells unless `--wrap` is set. Rule numbers are limited to 0–255, width to 240 columns, and output to 120 rows.

Elementary cellular automata use binary cells and update each cell from itself and its two nearest neighbors. The rule number encodes the eight possible neighborhoods; see [Wolfram MathWorld](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).

## License

MIT
