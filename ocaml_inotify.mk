V=0.5

SRC=$(OBJDIR)/ocaml_inotify-$(V)
PATCHES=ocaml-inotify-install

CFLAGS := -I/opt/xensource/lib/ocaml -L/opt/xensource/lib -I/opt/xensource/include
export CFLAGS

INOTIFY_DISTFILE=$(DISTFILES)/ocaml_inotify-$(V).tar.bz2

$(EXTRACTED):
	rm -rf $(SRC)
	cd $(OBJDIR) && tar -jxvf $(INOTIFY_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) all
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install
	@touch $@

$(SOURCES):
	echo ocaml lgpl file $(INOTIFY_DISTFILE) > $@

clean::
	rm -rf $(SRC)
