#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([arkimet-postprocess-bufr], [0.1], [edigiacomo@arpa.emr.it])
AM_INIT_AUTOMAKE([foreign])

AC_CONFIG_SRCDIR([configure.ac])
AC_CONFIG_HEADERS([config.h])
AC_PROG_CXX

AC_PATH_PROG([ARKI_XARGS], [arki-xargs])
if test x$ARKI_XARGS = x
then
	AC_MSG_ERROR([arki-xargs not found])
fi
AC_PATH_PROG([METEO_VM2_TO_BUFR], [meteo-vm2-to-bufr])
if test x$METEO_VM2_TO_BUFR = x
then
	AC_MSG_ERROR([meteo-vm2-to-bufr not found])
fi
AC_PATH_PROG([asciidoc], [asciidoc])
if test "x$asciidoc" = x
then
	AC_MSG_ERROR([asciidoc not found])
fi
AC_PATH_PROG([a2x], [a2x])
if test "x$a2x" = x
then
	AC_MSG_ERROR([a2x not found])
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
