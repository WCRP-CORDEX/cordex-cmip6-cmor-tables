# Welcome

This is a small collection of examples of how cmorized CORDEX-CMIP6 datasets could look like.

:::{note}
Current archive specifications for CORDEX-CMIP6 available under https://wcrp-cordex.github.io/archive-specifications
:::

## What does *cmorization* mean?

The process of rewriting climate model output (cmor) to a common intercomparable data model is usually referred to as *cmorization*.
The goal is to produce [CF-compliant](https://cfconventions.org/) inter-comparable climate model output for use in
model intercomparison projects (MIPs) like, e.g., [CMIP6](https://wcrp-cmip.org/cmip-phase-6-cmip6).
Usually, the [cmor](https://cmor.llnl.gov/) library is used which provides APIs for C, Fortran and python and
is also linked to, e.g., the [cmor operator](https://code.mpimet.mpg.de/projects/cdo/wiki/CDO_CMOR_Operator)
of the climate data operator tool (CDO).

Data and metadata conventions for a MIP are usually stored in the form of json tables that contain entries for each
variable and its metadata. Metadata is attached in the form of NetCDF variable or global attributes. Additionally,
data might have to be manipulated (e.g., unit conversion or conversion of precision)
