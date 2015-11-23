#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([arkimet-postprocess-subarea], [0.2], [edigiacomo@arpa.emr.it])
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

AC_PATH_PROG([asciidoc], [asciidoc])
if test "x$asciidoc" = x
then
	AC_MSG_ERROR([asciidoc not found])
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
