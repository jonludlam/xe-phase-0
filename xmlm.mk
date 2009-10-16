V=1.0.1

PATCHES=xmlm-install xmlm-do-not-display-none-dtd-on-output

NAME=xmlm-$(V)
PACKAGE=$(NAME).tbz
URL=http://erratique.ch/software/xmlm/releases/$(PACKAGE)

SRC=$(OBJDIR)/$(NAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	rm -rf $(SRC)
	cd $(OBJDIR) && tar -jxvf $(SRC_DIR)/$(PACKAGE)
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
	echo ocaml bsd file $(DISTFILES)/$(PACKAGE) > $@

clean::
	rm -rf $(SRC)
