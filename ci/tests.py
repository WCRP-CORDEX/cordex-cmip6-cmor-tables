import os
import shutil

import cordex as cx
import pytest
from cfchecker.cfchecks import CFChecker
from cordex import cmor as cxcmor

# import subprocess


table_dir = "./Tables"

cxcmor.set_options(table_prefix="CORDEX")


def copy_tables(table_dir):
    """copy CORDEX-CMIP6 table names to CMIP6 tables names
    This is because PrePARE does not allow us to give tables names.
    """
    import glob

    tables = glob.glob(os.path.join(table_dir, "*"))
    new_tables = []
    for src in tables:
        dst_path = os.path.dirname(src)
        base = os.path.basename(src)
        dst = os.path.join(dst_path, "CMIP6_" + "_".join(base.split("_")[1:]))
        # os.symlink(src, dst)
        shutil.copyfile(src, dst)
        new_tables.append(dst)
    return new_tables


def copy_filename_to_cmip6(filename):
    base = os.path.basename(filename)
    path = os.path.dirname(filename)
    elements = base.split("_")
    del elements[3]
    cmip6_filename = os.path.join(path, "_".join(elements))
    shutil.copyfile(filename, cmip6_filename)
    return cmip6_filename


def fx_file():
    ds = cx.cordex_domain("EUR-11", dummy="topo")
    filename = cxcmor.cmorize_variable(
        ds,
        "orog",
        mapping_table={"orog": {"varname": "topo"}},
        cmor_table=os.path.join(table_dir, "CORDEX_fx.json"),
        dataset_table=os.path.join(table_dir, "CORDEX_remo_example.json"),
        grids_table=os.path.join(table_dir, "CORDEX_grids.json"),
        CORDEX_domain="EUR-11",
        time_units=None,
        allow_units_convert=True,
    )
    return filename


def mon_file():
    ds = cx.tutorial.open_dataset("remo_EUR-11_TEMP2_mon")
    filename = cxcmor.cmorize_variable(
        ds,
        "tas",
        mapping_table={"tas": {"varname": "TEMP2"}},
        cmor_table=os.path.join(table_dir, "CORDEX_mon.json"),
        dataset_table=os.path.join(table_dir, "CORDEX_remo_example.json"),
        grids_table=os.path.join(table_dir, "CORDEX_grids.json"),
        CORDEX_domain="EUR-11",
        time_units=None,
        allow_units_convert=True,
    )
    return filename


@pytest.mark.parametrize("file", [fx_file(), mon_file()])
def test_cfchecker(file):
    print("checking file", file)
    checker = CFChecker()
    res = checker.checker(file)
    assert not res["global"]["ERROR"]
