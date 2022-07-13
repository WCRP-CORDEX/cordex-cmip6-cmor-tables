import os
import shutil
import subprocess

import cordex as cx
import pyremo as pr
import pytest
from pyremo import cmor as prcmor

table_dir = "./Tables"


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


@pytest.fixture
def fx_file():
    ds = pr.data.surflib("EUR-11")
    eur11 = cx.cordex_domain("EUR-11")
    ds = ds.assign_coords({"lon": eur11.lon, "lat": eur11.lat})
    filename = prcmor.cmorize_variable(
        ds,
        "orog",
        cmor_table=os.path.join(table_dir, "CORDEX-CMIP6_fx.json"),
        dataset_table=os.path.join(table_dir, "CORDEX-CMIP6_remo_example.json"),
        grids_table=os.path.join(table_dir, "CORDEX-CMIP6_grids.json"),
        CORDEX_domain="EUR-11",
        time_units=None,
        allow_units_convert=True,
    )
    return filename


def test_fx(fx_file):
    new_tables = copy_tables(table_dir)
    fx_file = copy_filename_to_cmip6(fx_file)
    print(fx_file)
    command = ["PrePARE", "--table-path", table_dir, fx_file]
    test = subprocess.run(command)
    for f in new_tables:
        os.remove(f)
    print("The exit code was: %d" % test.returncode)
    assert test.returncode == 0

    # return os.system(f"PrePARE --table-path ./Tables {fx_file}")


# def test_cmorizer_mon():
#    ds = pr.tutorial.open_dataset("remo_EUR-11_TEMP2_mon")
#    eur11 = cx.cordex_domain("EUR-11")
#    ds = ds.assign_coords({"lon": eur11.lon, "lat": eur11.lat})
#    filename = prcmor.cmorize_variable(
#        ds,
#        "tas",
#        cmor_table=os.path.join(table_dir, "CORDEX-CMIP6_mon.json"),
#        dataset_table=os.path.join(table_dir, "CORDEX-CMIP6_remo_example.json"),
#        CORDEX_domain="EUR-11",
#        time_units=None,
#        allow_units_convert=True,
#    )
#    output = xr.open_dataset(filename)
#    assert output.dims["time"] == 12
#    assert "tas" in output
#
#
# @pytest.mark.parametrize("table, tdim", [("CORDEX-CMIP6_day.json", 3), ("CORDEX-CMIP6_3hr.json", 17)])
# def test_cmorizer_subdaily(table, tdim):
#    ds = pr.tutorial.open_dataset("remo_EUR-11_TEMP2_1hr")
#    eur11 = cx.cordex_domain("EUR-11")
#    ds = ds.assign_coords({"lon": eur11.lon, "lat": eur11.lat})
#    filename = prcmor.cmorize_variable(
#        ds,
#        "tas",
#        cmor_table=os.path.join(table_dir, table),
#        dataset_table=os.path.join(table_dir, "CORDEX-CMIP6_remo_example.json"),
#        CORDEX_domain="EUR-11",
#        time_units=None,
#        allow_units_convert=True,
#        allow_resample=True,
#    )
#    output = xr.open_dataset(filename)
#    assert "tas" in output
#    assert output.dims["time"] == tdim
