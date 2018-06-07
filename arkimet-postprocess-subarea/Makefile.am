postprocdir = $(libdir)/arkimet

dist_postproc_SCRIPTS = $(srcdir)/subarea

TESTS = test-subarea.sh

dist_doc_DATA = README.asciidoc README.html

dist_man7_MANS = arkimet-postprocess-subarea.7

README.html: README.asciidoc
	asciidoc -a toc -o $(builddir)/$@ $<

arkimet-postprocess-subarea.7: README.asciidoc
	a2x -dmanpage -fmanpage -D $(builddir) $<

EXTRA_DIST = test-subarea.sh test.grib1 
