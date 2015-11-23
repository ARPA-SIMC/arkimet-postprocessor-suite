postprocdir = $(libdir)/arkimet

postproc_SCRIPTS = bufr

bufr: bufr.in
	sed -e 's,[@]PKGLIBDIR[@],$(pkglibexecdir),g' $< > $@

nodist_doc_DATA = \
		  arkimet-postprocess-bufr.7.txt \
		  arkimet-postprocess-bufr.7.html

nodist_man7_MANS = \
		   arkimet-postprocess-bufr.7

%.7.txt: %.7.txt.in
	sed \
		-e 's,[@]PKGLIBDIR[@],$(pkglibexecdir),g' \
		-e 's,[@]POSTPROCDIR[@],$(postprocdir),g' \
		$< > $@

%.7.html: %.7.txt
	asciidoc -a toc $<

%.7: %.7.txt
	a2x -dmanpage -fmanpage $<

EXTRA_DIST = \
	     bufr.in \
	     arkimet-postprocess-bufr.7.txt.in

CLEANFILES = \
	     bufr \
	     arkimet-postprocess-bufr.7.txt \
	     arkimet-postprocess-bufr.7.html \
	     arkimet-postprocess-bufr.7.xml \
	     arkimet-postprocess-bufr.7
