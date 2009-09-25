V=3.11.0

SRC=$(OBJDIR)/ocaml-$(V)
#PATCHES=ocaml-get-backtrace

OCAML_DISTFILE=$(DISTFILES)/ocaml-$(V).tar.bz2

$(EXTRACTED):
	cd $(OBJDIR) && tar -jxf $(OCAML_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	cd $(SRC) && ./configure -prefix $(PREFIX)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) world.opt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) PREFIX=$(DESTDIR)$(PREFIX) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(OCAML_DISTFILE) > $@

clean::
	rm -rf $(SRC)
