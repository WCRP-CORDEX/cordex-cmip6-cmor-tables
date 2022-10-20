import json
from os import path as op

path = op.join(op.dirname(__file__), "../Tables")

tables = ["1hr", "6hr", "day", "mon"]

files = [op.join(path, f"CORDEX-CMIP6_{t}.json") for t in tables]

height = {
    "standard_name": "height",
    "units": "m",
    "axis": "Z",
    "long_name": "height",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "height",
    "positive": "up",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


pressure = {
    "standard_name": "air_pressure",
    "units": "Pa",
    "axis": "Z",
    "long_name": "pressure",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "plev",
    "positive": "down",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


longitude = {
    "standard_name": "longitude",
    "units": "degrees_east",
    "axis": "X",
    "long_name": "Longitude",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "yes",
    "out_name": "lon",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "360.0",
    "valid_min": "0.0",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


def dims_from_table(table):
    with open(table) as f:
        d = json.load(f)["variable_entry"]
    dims = []
    for v in d.values():
        if "dimensions" in v:
            dims.append(v["dimensions"])
    return dims


def unique_dims(dims):
    res = []
    for dim in dims:
        coords = dim.split(" ")
        for c in coords:
            if c not in res:
                res.append(c)
    return res


def unique_dims_from_tables(tables):
    dims = []
    for t in tables:
        print(t)
        dims.extend(dims_from_table(t))
    return unique_dims(dims)


def run():
    dims = unique_dims_from_tables(files)
    print(f"found: {dims}")


if __name__ == "__main__":
    run()
