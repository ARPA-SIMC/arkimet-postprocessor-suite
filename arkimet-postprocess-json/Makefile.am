postprocdir = $(libdir)/arkimet

pkgdocdir = $(docdir)/json

postproc_SCRIPTS = json

pkglibexec_SCRIPTS = bufr2chunks

json: json.in
	sed -e 's,[@]PKGLIBDIR[@],$(pkglibexecdir),g' $< > $@

dist_pkgdoc_DATA = README.asciidoc README.html

dist_man7_MANS = arkimet-postprocess-json.7

README.html: README.asciidoc
	asciidoc -a toc -o $(builddir)/$@ $<

arkimet-postprocess-json.7: README.asciidoc
	a2x -dmanpage -fmanpage -D $(builddir) $<

EXTRA_DIST = json.in bufr2chunks

CLEANFILES = json
