# Antipsychotic Switching Tool

Simple CLI D2-antagonist switching tool, currently supporting:
- Dose conversion (information by [The American Association of Psychiatric Pharmacists (AAPP)]).
- Half-life and CYP450 metabolsim enzymes (information by [DRUGBANK]).
- CSV integration (must use standard columns).

## Coming Soon
- Depot doses
- Switching taper

## Running

AST requires [Python] to run.

```sh
cd ast
python ast.py (path to csv)
```

## CSV File

Required rows:
- Drug (str)
- generation (str)
- defined_daily_dose (float)
- effective_dose_95 (float)
- minimum_effective_dose (float)
- half-life (str)
- CYP450 (str)

## License
[GNU General Public License v3.0]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [The American Association of Psychiatric Pharmacists (AAPP)]: <https://aapp.org/guideline/essentials/antipsychotic-dose-equivalents>
   [Python]: <https://www.python.org/>
   [DRUGBANK]: <https://go.drugbank.com/>
   [public repository]: https://github.com/patriciogtrz/ast
   [GNU General Public License v3.0]: <https://choosealicense.com/licenses/gpl-3.0/>
