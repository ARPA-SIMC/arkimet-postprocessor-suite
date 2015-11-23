postprocdir = $(libdir)/arkimet

dist_postproc_SCRIPTS = $(top_srcdir)/subarea

TESTS = test-subarea.sh

nodist_doc_DATA = \
		  arkimet-postprocess-subarea.7.txt \
		  arkimet-postprocess-subarea.7.html

nodist_man7_MANS = arkimet-postprocess-subarea.7

arkimet-postprocess-subarea.7.txt: arkimet-postprocess-subarea.7.txt.in
	cp $< $@

arkimet-postprocess-subarea.7.html: arkimet-postprocess-subarea.7.txt
	asciidoc -a toc $<

arkimet-postprocess-subarea.7: arkimet-postprocess-subarea.7.txt
	a2x -dmanpage -fmanpage -D $(builddir) $<

EXTRA_DIST = \
	     test-subarea.sh \
	     test.grib1 \
	     arkimet-postprocess-subarea.7.txt.in

CLEANFILES = \
	     arkimet-postprocess-subarea.7.txt \
	     arkimet-postprocess-subarea.7.html \
	     arkimet-postprocess-subarea.7 \
	     arkimet-postprocess-subarea.7.xml

