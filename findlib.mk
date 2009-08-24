V=1.1.2pl1

NAME=findlib-$(V)
PACKAGE=$(NAME).tar.gz
URL=http://www.ocaml-programming.de/packages/$(PACKAGE)

SRC=$(OBJDIR)/$(NAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	cd $(OBJDIR) && tar -zxf $(SRC_DIR)/$(PACKAGE)
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
