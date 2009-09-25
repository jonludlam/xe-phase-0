V=2.2

SRC=$(OBJDIR)/xml-light
PATCHES=xml-light-install xml-light-parse-fix xml-light-meta

XML_DISTFILE=$(DISTFILES)/xml-light-$(V).zip

$(EXTRACTED):
	rm -rf $(SRC)
	cd $(OBJDIR) && unzip $(XML_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) all opt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(XML_DISTFILE) > $@

clean::
	rm -rf $(SRC)
