# Arkimet postprocessors suite

## Build status

| Environment | Status |
| ----------- | ------ |
| CentOS 7    | [![Build Status](https://badges.herokuapp.com/travis/ARPA-SIMC/arkimet-postprocessor-suite?branch=master&env=DOCKER_IMAGE=centos:7&label=centos7)](https://travis-ci.org/ARPA-SIMC/arkimet-postprocessor-suite) |
| Fedora 27   | [![Build Status](https://badges.herokuapp.com/travis/ARPA-SIMC/arkimet-postprocessor-suite?branch=master&env=DOCKER_IMAGE=fedora:27&label=fedora27)](https://travis-ci.org/ARPA-SIMC/arkimet-postprocessor-suite) |
| Fedora 28   | [![Build Status](https://badges.herokuapp.com/travis/ARPA-SIMC/arkimet-postprocessor-suite?branch=master&env=DOCKER_IMAGE=fedora:28&label=fedora28)](https://travis-ci.org/ARPA-SIMC/arkimet-postprocessor-suite) |


## Arkimet postprocessors

- `subarea`: crop GRIB data given a bounding box
- `singlepoint`: extract a point from GRIB
- `bufr`: convert data to BUFR
- `json`: convert data to JSON
- `bufr-filter`: filter BUFR data
