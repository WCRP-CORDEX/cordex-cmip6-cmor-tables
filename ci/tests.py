import pytest
import pyremo as pr
import cordex as cx
import xarray as xr
from pyremo import cmor as prcmor
import os


table_dir = "./Tables"


def test_cmorizer_fx():
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
    output = xr.open_dataset(filename)
    assert "orog" in output


#def test_cmorizer_mon():
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
#@pytest.mark.parametrize("table, tdim", [("CORDEX-CMIP6_day.json", 3), ("CORDEX-CMIP6_3hr.json", 17)])
#def test_cmorizer_subdaily(table, tdim):
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
