postprocdir = $(libdir)/arkimet

postproc_SCRIPTS = json

pkglibexec_SCRIPTS = bufr2chunks

json: json.in
	sed -e 's,[@]PKGLIBDIR[@],$(pkglibexecdir),g' $< > $@

nodist_doc_DATA = \
		  arkimet-postprocess-json.7.txt \
		  arkimet-postprocess-json.7.html

nodist_man7_MANS = \
		   arkimet-postprocess-json.7

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
	     json.in \
	     bufr2chunks \
	     arkimet-postprocess-json.7.txt.in

CLEANFILES = \
	     json \
	     arkimet-postprocess-json.7.txt \
	     arkimet-postprocess-json.7.html \
	     arkimet-postprocess-json.7.xml \
	     arkimet-postprocess-json.7
