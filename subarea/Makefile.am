postprocdir = $(libdir)/arkimet

dist_postproc_SCRIPTS = $(top_srcdir)/subarea

TESTS = test-subarea.sh

nodist_man7_MANS = arkimet-postprocess-subarea.7

arkimet-postprocess-subarea.7.html: arkimet-postprocess-subarea.7.md
	pandoc -s $< -o $@

arkimet-postprocess-subarea.7: arkimet-postprocess-subarea.7.md
	pandoc -s -t man $< -o $@

EXTRA_DIST = \
	     test-subarea.sh \
	     test.grib1 \
	     arkimet-postprocess-subarea.7.md

CLEANFILES = \
	     arkimet-postprocess-subarea.7.html \
	     arkimet-postprocess-subarea.7
