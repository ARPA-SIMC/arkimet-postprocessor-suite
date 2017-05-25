postprocdir = $(libdir)/arkimet

dist_postproc_SCRIPTS = bufr-filter

dist_doc_DATA = README.asciidoc README.html arkimet-postprocess-bufr-filter.7

README.html: README.asciidoc
	asciidoc -a toc -o $(builddir)/$@ $<

arkimet-postprocess-bufr-filter.7: README.asciidoc
	a2x -dmanpage -fmanpage -D $(builddir) $<
