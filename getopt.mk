V=20040811

SRC=$(OBJDIR)/getopt
PATCHES=getopt-install

GETOPT_DISTFILE=$(DISTFILES)/getopt-$(V).tar.gz

$(EXTRACTED):
	cd $(OBJDIR) && tar -zxf $(GETOPT_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) all allopt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(GETOPT_DISTFILE) > $@
	
clean::
	rm -rf $(SRC)
