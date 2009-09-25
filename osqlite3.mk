# ocaml_sqlite3-0.1.tar.bz2
V=0.2

SRC=$(OBJDIR)/ocaml_sqlite3-$(V)
PATCHES=osqlite3-install

CFLAGS := -I/opt/xensource/lib/ocaml -L/opt/xensource/lib -I/opt/xensource/include
export CFLAGS

OSQLITE_DISTFILE := $(DISTFILES)/ocaml_sqlite3-$(V).tar.bz2

$(EXTRACTED):
	cd $(OBJDIR) && tar -jxf $(OSQLITE_DISTFILE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) libs
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) DESTDIR=$(DESTDIR) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(OSQLITE_DISTFILE) > $@

clean::
	rm -rf $(SRC)
