LANG ?= no
SRC := $(wildcard book/$(LANG)/*.md)
BUILD := build/$(LANG)
TITLE := Ploos IRC Handbook

.PHONY: all html epub kindle pdf clean

all: html epub kindle pdf

$(BUILD):
	mkdir -p $(BUILD)

html: $(BUILD)
	pandoc $(SRC) --standalone --toc --metadata title="$(TITLE)" -o $(BUILD)/irc-handbook.html

epub: $(BUILD)
	pandoc $(SRC) --toc --metadata title="$(TITLE)" -o $(BUILD)/irc-handbook.epub

# Modern Kindle workflows accept EPUB. This target produces a dedicated
# Kindle-ready EPUB artifact so later validation/conversion can evolve
# independently from the general EPUB build.
kindle: $(BUILD)
	pandoc $(SRC) --toc --metadata title="$(TITLE)" -o $(BUILD)/irc-handbook-kindle.epub

pdf: $(BUILD)
	pandoc $(SRC) --toc --metadata title="$(TITLE)" --pdf-engine=xelatex -o $(BUILD)/irc-handbook.pdf

clean:
	rm -rf build
