# arkimet-postprocessor-suite
Arkimet postprocessors

## Subarea
Crop a subarea of a GRIB file. The 4 parameters are `MINLON`, `MINLAT`,
`MAXLON`, `MAXLAT`.

Synopsys: `subarea MINLON MINLAT MAXLON MAXLAT`

    # Subarea SW=12,43 NE=14,44
    arki-query --postproc="subarea 12 43 14 44" QUERY DATASET

## Singlepoint
Get a single point (`LON`, `LAT`) from a GRIB file in BUFR, CREX or JSON format.

Synopsys: `singlepoint [-z near|bilin] [-f bufr|crex|geojson|dbajson] LON LAT`

    # BUFR point 12,45 using nearest point
    arki-query --postproc="singlepoint -z near -f bufr 12 45" QUERY DATASET
    # CREX point 12,45 using bilinear transformation
    arki-query --postproc="singlepoint -z near -f crex 12 45" QUERY DATASET
    # GeoJSON point 12,45 using nearest point
    arki-query --postproc="singlepoint -z near -f geojson 12 45" QUERY DATASET
    # DB-All.e JSON point 12,45 using nearest point
    arki-query --postproc="singlepoint -z near -f dbajson 12 45" QUERY DATASET

## JSON
Convert data to JSON (GeoJSON or DB-All.e JSON) and filter data with ARPA-SIMC
quality control.

Synopsys: `json [-t dbajson|geojson] [-f skip|none|preserve]`

    # DB-All.e JSON without quality control filter
    arki-query --postproc="json -t dbajson -f none" QUERY DATASET
    # GeoJSON without "wrong" data
    arki-query --postproc="json -t geojson -f skip" QUERY DATASET
    # DB-All.e JSON with preserved "wrong" data and a summary attribute (B33007=0)
    arki-query --postproc="json -t dbajson -f preserve" QUERY DATASET

## BUFR
Convert data to BUFR.

Synopsys: `bufr`.
