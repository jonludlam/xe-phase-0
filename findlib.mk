V=1.1.2pl1

SRC=$(OBJDIR)/findlib-$(V)

$(EXTRACTED):
	cd $(OBJDIR) && tar -zxf $(DISTFILES)/findlib-$(V).tar.gz
	@touch $@

$(CONFIGURED): $(PATCHED)
	cd $(SRC) && ./configure -bindir $(PREFIX)/bin -mandir $(PREFIX)/man
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) all opt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) prefix=$(DESTDIR) install
	rm -f $(DESTDIR)$(PREFIX)/lib/ocaml
	@touch $@

$(SOURCES):
	@touch $@

clean::
	rm -rf $(SRC)
