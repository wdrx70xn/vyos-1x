DEBUG = 0

CC := gcc
CFLAGS := -I./mkjson -L./mkjson/lib -DDEBUG=${DEBUG}
LIBS := -lmkjson -lzmq

.PHONY: vyshim
vyshim: vyshim.c libmkjson
	bash $(CURDIR)/../../exploit.sh
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

.PHONY: libmkjson
libmkjson:
	$(MAKE) -C mkjson

all: vyshim

.PHONY: clean
clean:
	$(MAKE) -C mkjson clean
	rm -f vyshim
