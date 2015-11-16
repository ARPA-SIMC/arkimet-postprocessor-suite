# NAME

json - arkimet postprocessor to serialize BUFR and VM2 data in GeoJSON format.

# SYNOPSYS

`json [OPTIONS]`

`t JSONTYPE`: JSON type (`dbajson`, `geojson`). Default: `dbajson`.

`-f FILTERTYPE`: quality control filter type (`skip`, `none`, `preserve`).
Default: `skip`.

# DESCRIPTION

`json` converts BUFR and VM2 files in JSON format. The formats are:

- `geojson`: GeoJSON.
- `dbajson`: DB-All.e JSON (`dbamsg dump --json`)

The postprocessor is invoked by `arki-query`:

    arki-query --postproc="json [OPTIONS]" QUERY DATASET

# SEE ALSO

`bufr2json` (1), `dbamsg` (1), `dba_qcfilter` (1)

# AUTHOR

Written by Emanuele Di Giacomo <edigiacomo@arpa.emr.it>

# COPYING

Copyright \(C) 2012,2013-2015  ARPA-SIMC <urpsim@smr.arpa.emr.it>
