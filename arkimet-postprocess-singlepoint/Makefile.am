postprocdir = $(libdir)/arkimet

postproc_SCRIPTS = singlepoint

TESTS = test-singlepoint.sh

nodist_doc_DATA = \
		  arkimet-postprocess-singlepoint.7.txt \
		  arkimet-postprocess-singlepoint.7.html

nodist_man7_MANS = arkimet-postprocess-singlepoint.7

arkimet-postprocess-singlepoint.7.txt: arkimet-postprocess-singlepoint.7.txt.in
	cp $< $@

arkimet-postprocess-singlepoint.7.html: arkimet-postprocess-singlepoint.7.txt
	$(ASCIIDOC) -a toc $<

arkimet-postprocess-singlepoint.7: arkimet-postprocess-singlepoint.7.txt
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

EXTRA_DIST = \
	     singlepoint.in \
	     test-singlepoint.sh.in \
	     test.grib1 \
	     arkimet-postprocess-singlepoint.7.txt.in

CLEANFILES = \
	     singlepoint \
	     test-singlepoint.sh \
	     arkimet-postprocess-singlepoint.7.txt \
	     arkimet-postprocess-singlepoint.7.html \
	     arkimet-postprocess-singlepoint.7 \
	     arkimet-postprocess-singlepoint.7.xml

