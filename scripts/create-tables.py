import argparse

import data_request as dr
import pandas as pd


def main(table, output, prefix="CORDEX-CMIP6"):
    df = pd.read_csv(table).fillna("")
    cmor_tables = dr.create_cmor_tables(df)
    print(cmor_tables.keys())

    for t in cmor_tables.values():
        dr.table_to_json(t, table_prefix="CORDEX-CMIP6", dir=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("table", help="data request csv table")
    parser.add_argument("--prefix", help="table prefix", default="CORDEX-CMIP6")
    parser.add_argument("--output", help="output directory", default="Tables")
    args = parser.parse_args()
    main(args.table, args.output, args.prefix)
