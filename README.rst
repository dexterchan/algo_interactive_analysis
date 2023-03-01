====================
interactive_analysis
====================


.. image:: https://img.shields.io/pypi/v/interactive_analysis.svg
        :target: https://pypi.python.org/pypi/interactive_analysis

.. image:: https://img.shields.io/travis/dexterchan/interactive_analysis.svg
        :target: https://travis-ci.com/dexterchan/interactive_analysis

.. image:: https://readthedocs.org/projects/interactive-analysis/badge/?version=latest
        :target: https://interactive-analysis.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Interactively work with algo result with Pandas


* Free software: MIT license
* Documentation: https://interactive-analysis.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

```
conda create --name interactive_analysis python=3.9
```

# Test
```
export PYTHONPATH=src
export ANALYSIS_CONFIG_PATH=resources/.secret/analysis_config.json
```

sample of analysis_config.json
```
{
    "strategy_calculation_log_directory": "file:///var/task/data/calc_log_data",
    "pnl_result_conn_str": "postgresql://droid:xxx@x.x.x.x:5432/crypto",
    "strategy_conn_str": "postgresql://droid:xxx@x.x.x.x:5432/crypto",
    "live_trade_signal_conn_str": "postgresql://droid:xxx@x.x.x.x:5432/crypto"
}
```