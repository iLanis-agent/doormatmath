# Doormat math

The mat size that actually catches two footfalls, the kilograms of grit a year it stops, and the hours a soaked mat takes to dry. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/doormatmath/

## The three tools

- **Size plan** - `sizePlan(doorWCm, extraCm, strideCm)`: width and depth for a mat that scrapes.
- **Grit plan** - `gritPlan(stepsPerVisit, visitsPerDay, gPerStep)`: grams a day and kilograms a year.
- **Dry plan** - `dryPlan(matLCm, matWCm, mlPerM2, evapMlHour)`: area, held water and drying hours.

## Labeled norms (illustrative references, not rules)

- Extra width: 10 cm a side. Stride: 65 cm, caught twice. Grit: 0.4 g a step. Soak: 1000 ml per m², drying at 100 ml an hour. Your door, boots and weather decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (14 cases, 61 checks)

Regenerate the oracle expectations: `python3 oracle.py`
