postprocdir = $(libdir)/arkimet

pkgdocdir = $(docdir)/bufr

dist_postproc_SCRIPTS = bufr

dist_pkgdoc_DATA = README.asciidoc README.html

dist_man7_MANS = arkimet-postprocess-bufr.7

README.html: README.asciidoc
	asciidoc -a toc -o $(builddir)/$@ $<

arkimet-postprocess-bufr.7: README.asciidoc
	a2x -dmanpage -fmanpage -D $(builddir) $<
