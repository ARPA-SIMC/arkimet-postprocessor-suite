#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([arkimet-postprocessor-suite], [0.1], [edigiacomo@arpa.emr.it])
AM_INIT_AUTOMAKE([foreign])

AC_PATH_PROG([ARKI_XARGS], [arki-xargs])
if test x$ARKI_XARGS = x
then
	AC_MSG_ERROR([arki-xargs not found])
fi
AC_PATH_PROG([VG6D_SUBAREA], [vg6d_subarea])
if test x$VG6D_SUBAREA = x
then
	AC_MSG_ERROR([vg6d_subarea not found])
fi
AC_PATH_PROG([BUFR2JSON], [bufr2json])
if test x$BUFR2JSON = x
then
    AC_MSG_ERROR([bufr2json not found])
fi
AC_PATH_PROG([METEO_VM2_TO_BUFR], [meteo-vm2-to-bufr])
if test x$METEO_VM2_TO_BUFR = x
then
    AC_MSG_ERROR([meteo-vm2-to-bufr not found])
fi

AC_CONFIG_FILES([Makefile
                 subarea/Makefile
                 singlepoint/Makefile])
AC_OUTPUT
