V=r26

SRC=$(OBJDIR)/annot-$(V)

$(EXTRACTED):
	tar -C $(OBJDIR) -jxf $(DISTFILES)/annot-$(V).tar.bz2
	@touch $@

$(CONFIGURED): $(PATCHED)
	cd $(SRC) && ./configure --prefix=$(PREFIX)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) MAKEFILES=
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install MAKEFILES= BINDIR=$(DESTDIR)$(PREFIX)/bin \
		MAN1DIR=$(DESTDIR)$(PREFIX)/man/man1
	@touch $@

$(SOURCES):
	@touch $@

clean::
	rm -rf $(SRC)
