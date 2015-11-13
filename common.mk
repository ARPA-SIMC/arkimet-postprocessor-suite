SUFFIXES = .7.html .7 .7.md

.7.md.7.html:
	pandoc -s $< -o $@

.7.md.7:
	pandoc -s -t man $< -o $@

postprocdir = $(libdir)/arkimet
