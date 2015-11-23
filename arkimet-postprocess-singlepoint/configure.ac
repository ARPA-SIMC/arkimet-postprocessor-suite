#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([arkimet-postprocess-singlepoint], [0.3], [edigiacomo@arpa.emr.it])
AM_INIT_AUTOMAKE([foreign])

AC_PATH_PROG([ARKI_XARGS], [arki-xargs])
if test x$ARKI_XARGS = x
then
	AC_MSG_ERROR([arki-xargs not found])
fi
AC_PATH_PROG([VG6D_GETPOINT], [vg6d_getpoint])
if test x$VG6D_GETPOINT = x
then
	AC_MSG_ERROR([vg6d_getpoint not found])
fi
AC_PATH_PROG([BUFR2JSON], [bufr2json])
if test x$BUFR2JSON = z
then
	AC_MSG_ERROR([bufr2json not found])
fi
AC_PATH_PROG([ASCIIDOC], [asciidoc])
if test "x$ASCIIDOC" = x
then
	AC_MSG_ERROR([asciidoc not found])
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
