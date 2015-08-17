# leave these lines alone
.SUFFIXES: .erl .beam .yrl

.erl.beam :
	erlc -W $<

.yrl.erl :
	erlc -W $<

ERL = erl -boot start_clean

#MODS = module1 module \
#	module3 \
#	moduleN

all : compile

#compile : ${MODS:%=%.beam} subdirs
compile : ${%=%.beam} subdirs

special1.beam : special1.erl
	${ERL} -Dflag1 -W0 special1.erl

application1 : compile
	${ERL} -pa Dirl -s application1 start Arg1 Arg2

subdirs :
	#cd dir1; $(MAKE)
	#$(MAKE) -C dir2

# remove all the code
clean :
	rm -rf *.beam erl_crash.dump
	cd dir1; $(MAKE) clean
	$(MAKE) -C dir2 clean

escript : compile
	escript script


