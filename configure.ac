#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([arkimet-postprocess-suite], [0.1], [edigiacomo@arpae.it])
AM_INIT_AUTOMAKE([foreign])

AC_CONFIG_SRCDIR([configure.ac])

# all
AC_PATH_PROG([ARKI_XARGS], [arki-xargs])
if test x$ARKI_XARGS = x
then
    AC_MSG_ERROR([arki-xargs not found])
fi

# bufr json
AC_PATH_PROG([METEO_VM2_TO_BUFR], [meteo-vm2-to-bufr])
if test x$METEO_VM2_TO_BUFR = x
then
    AC_MSG_ERROR([meteo-vm2-to-bufr not found])
fi

# bufr-filter
AC_PATH_PROG([ARKI_XARGS], [dbadb])
if test x$ARKI_XARGS = x
then
    AC_MSG_ERROR([dbadb not found])
fi

# subarea
AC_PATH_PROG([VG6D_SUBAREA], [vg6d_subarea])
if test x$VG6D_SUBAREA = x
then
AC_MSG_ERROR([vg6d_subarea not found])
fi

# json singlepoint
AC_PATH_PROG([VG6D_GETPOINT], [vg6d_getpoint])
if test x$VG6D_GETPOINT = x
then
    AC_MSG_ERROR([vg6d_getpoint not found])
fi

# json
AC_PATH_PROG([DBA_QCFILTER], [dba_qcfilter])
if test x$DBA_QCFILTER = x
then
    AC_MSG_ERROR([dba_qcfilter not found])
fi

# json singlepoint
AC_PATH_PROG([BUFR2JSON], [bufr2json])
if test x$BUFR2JSON = x
then
    AC_MSG_ERROR([bufr2json not found])
fi

# json
AC_PATH_PROG([DBAMSG], [dbamsg])
if test x$DBAMSG = x
then
	AC_MSG_ERROR([dbamsg not found])
fi


# all
AC_PATH_PROG([asciidoc], [asciidoc])
if test "x$asciidoc" = x
then
    AC_MSG_ERROR([asciidoc not found])
fi

# all
AC_PATH_PROG([a2x], [a2x])
if test "x$a2x" = x
then
    AC_MSG_ERROR([a2x not found])
fi

AC_CONFIG_FILES([Makefile
                 arkimet-postprocess-bufr-filter/Makefile
                 arkimet-postprocess-bufr/Makefile
                 arkimet-postprocess-json/Makefile
                 arkimet-postprocess-singlepoint/Makefile
                 arkimet-postprocess-subarea/Makefile])
AC_OUTPUT
