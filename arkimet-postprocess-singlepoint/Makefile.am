postprocdir = $(libdir)/arkimet

pkgdocdir = $(docdir)/singlepoint

postproc_SCRIPTS = singlepoint

TESTS = test-singlepoint.sh

dist_pkgdoc_DATA = README.asciidoc README.html

dist_man7_MANS = arkimet-postprocess-singlepoint.7

README.html: README.asciidoc
	asciidoc -a toc -o $(builddir)/$@ $<

arkimet-postprocess-singlepoint.7: README.asciidoc
	a2x -dmanpage -fmanpage -D $(builddir) $<

singlepoint: singlepoint.in
	sed \
		-e "s,[@]BUFR2JSON[@],$(BUFR2JSON),g" \
		-e "s,[@]ARKI_XARGS[@],$(ARKI_XARGS),g" \
		-e "s,[@]VG6D_GETPOINT[@],$(VG6D_GETPOINT),g" \
		$< > $@
	chmod ugo+x $@

test-singlepoint.sh: test-singlepoint.sh.in
	sed \
		-e "s,[@]srcdir[@],$(srcdir),g" \
		-e "s,[@]builddir[@],$(builddir),g" \
		$< > $@
	chmod ugo+x $@

EXTRA_DIST = singlepoint.in test-singlepoint.sh.in test.grib1

CLEANFILES = singlepoint test-singlepoint.sh
