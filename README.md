# cordex-cmip6-cmor-tables

[![cfchecks](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/actions/workflows/cfchecks.yaml/badge.svg)](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/actions/workflows/cfchecks.yaml)
[![deploy examples](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/actions/workflows/deploy-examples.yaml/badge.svg)](https://wcrp-cordex.github.io/cordex-cmip6-cmor-tables/cmor-examples.html)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/WCRP-CORDEX/cordex-cmip6-cmor-tables/main.svg)](https://results.pre-commit.ci/latest/github/WCRP-CORDEX/cordex-cmip6-cmor-tables/main)
[![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/WCRP-CORDEX/binder-sandbox/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252FWCRP-CORDEX%252Fcordex-cmip6-cmor-tables%26urlpath%3Dlab%252Ftree%252Fcordex-cmip6-cmor-tables%252Fexamples%252Fcmor-examples.ipynb%26branch%3Dmain)

JSON Tables for CMOR3 to create CORDEX-CMIP6 datasets.

## Table update

These tables are created from the [CORDEX-CMIP6 data request table](https://github.com/WCRP-CORDEX/data-request-table) using:

```bash
pip install git+https://github.com/WCRP-CORDEX/data-request-tools.git
```
and
```bash
python scripts/create-tables.py https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/refs/heads/main/cmor-table/datasets.csv
```

## Registering Institutions, Models, or requesting changes to CVs:

For registering your institution or model, please submit an issue in the [CV repository](https://github.com/WCRP-CORDEX/cordex-cmip6-cv) using these forms:

* [New institution_id](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/issues/new?assignees=&labels=Register+institution-id&projects=&template=institution_id.yaml&title=institution_id+registration+of+...)
* [New source_id (i.e. model)](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/issues/new?assignees=&labels=Register+source-id&projects=&template=source_id.yaml&title=source_id+registration+of+...)

These forms will automatically create a pull request, where further details can be discussed.

## Current Issues

Note that there might be some issues if your are using the [cmor library](https://github.com/PCMDI/cmor) with these tables, for example:

* The [archive specifications](https://zenodo.org/records/10961069) recommed to use `crs` as the name of the grid mapping variable. However, using cmor, it doensn't seem to be possible to properly adapt the grid mapping's variable name (https://github.com/WCRP-CORDEX/archive-specifications/issues/17).
* In your input dataset json file, make sure the `_cmip6_option` is removed so that more flexible CV's are possible. See also [this discussion](https://github.com/PCMDI/cmor/discussions/679#discussioncomment-3842958). You can also check the [example input file](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/blob/main/Tables/CORDEX-CMIP6_remo_example.json).
* Make sure to use `cmor>=3.8.0` since `CORDEX-CMIP6` does not require the `further_info_url`, see also https://github.com/PCMDI/cmor/pull/727. Otherwise, a default `further_info_url` will be added by cmor that is created from related attributes but will probably point to an invalid URL.
* UPDATE: resolved since [3.9.0](https://github.com/PCMDI/cmor/releases/tag/3.9.0) ~~With the current cmor release (`3.8.0`), a [default realm attribute](https://github.com/PCMDI/cmor/issues/736) is written, although not required by the CV. This is fixed in an upcoming cmor release.~~
* Finally, if you use these tables together with the cmor library and successfully create cmorized files, it is still not guaranteed that you used the CV correctly. This is unfortunately but reasonably due to the close relation between cmor and the original CMIP6 requirements for AR6. This means, e.g., that CV entries other than the basic `insitution_id` or `source_id` are not as rigorously checked but mainly only for their presence if they are part of the required global attributes. For example, only attributes in the CV that are defined as lists are checked for consistency but not if they are defined as subsections. For some more details on this issue, please follow https://github.com/PCMDI/cmor/discussions/679#discussioncomment-3889102.

## Feedback

If you have any issues regarding the cmor tables, please open an issue. If you have an issue regarding the data request, e.g., variable metadata, please check [here](https://github.com/WCRP-CORDEX/data-request-table/issues). For issues regarding the controlled vocabulary, please check [here](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/issues).
