V=0.9.0

SRC=$(OBJDIR)/xmlm-$(V)
PATCHES=xmlm-install

XML_DISTFILE=$(DISTFILES)/xmlm-$(V).tbz

$(EXTRACTED):
	rm -rf $(SRC)
	cd $(OBJDIR) && tar -jxvf $(XML_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) default
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install
	@touch $@

$(SOURCES):
	echo ocaml bsd file $(XML_DISTFILE) > $@

clean::
	rm -rf $(SRC)
