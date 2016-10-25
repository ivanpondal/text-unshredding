TEXTS = engadget.txt atom.txt

build: LKH-2.0.7/LKH shredded_texts build_message

reconstruct: $(foreach text,$(TEXTS),$(patsubst %,texts/reconstructed/%,$(text))) reconstruct_message

clean:
	rm -rf texts/shredded/* tsp/*/* LKH-2.0.7 bin/compute_scores

shredded_texts: $(foreach text,$(TEXTS),$(patsubst %,texts/shredded/%,$(text)))

build_message:
	@echo
	@echo "Now run 'make reconstruct' to reconstruct the texts"

reconstruct_message:
	@echo
	@echo "The reconstructed texts are in texts/reconstructed"

.PHONY: build reconstruct clean shredded_texts build_message reconstruct_message
.SECONDARY: # Retain all intermediate files

LKH-2.0.7/Makefile:
	curl -L http://webhotel4.ruc.dk/~keld/research/LKH/LKH-2.0.7.tgz | tar zxf -

LKH-2.0.7/LKH: LKH-2.0.7/Makefile
	$(MAKE) -C LKH-2.0.7

tsp/instances/%.tsp: texts/shredded/%.txt src/compute_column_score.py
	cat $< | src/compute_column_score.py data/letter_proximity.csv > $@

tsp/tours/%.tour: tsp/instances/%.tsp LKH-2.0.7/LKH bin/lkh.sh
	bin/lkh.sh $< $@

texts/shredded/%.txt: texts/original/%.txt src/text_shredder.py
	cat $< | src/text_shredder.py > $@

texts/reconstructed/%.txt: tsp/tours/%.tour src/text_unshredder.py
	cat texts/shredded/$*.txt | src/text_unshredder.py tsp/tours/$*.tour > $@
