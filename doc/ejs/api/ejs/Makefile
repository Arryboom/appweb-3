#
#	Makefile -- Ejscript API Documentation
#
#	Copyright (c) Embedthis Software LLC, 2003-2012. All Rights Reserved.
#

include		.makedep

doc:
	rm ../../../all/*.c
	make -C ../../../all
	rm -fr xml html
	mkdir -p xml html
	doxygen ejs.spec
	ejs $(BLD_TOOLS_DIR)/gendoc.es --bare --title "Escript Native API" --tags ../ejs.tags \
		xml/ejs_8h.xml xml/group* xml/struct_*.xml >../ejsBare.html
	ejs $(BLD_TOOLS_DIR)/gendoc.es --title "Ejscript Native API" --tags ../ejs.tags \
		xml/ejs_8h.xml xml/group* xml/struct_*.xml >../ejs.html

x:
	echo HERE
	echo ejs $(BLD_TOOLS_DIR)/gendoc.es --bare --title "Escript Native API" --tags ../ejs.tags \
		xml/ejs_8h.xml xml/group* xml/struct_*.xml
	ejs $(BLD_TOOLS_DIR)/gendoc.es --bare --title "Escript Native API" --tags ../ejs.tags \
		xml/ejs_8h.xml xml/group* xml/struct_*.xml >../ejsBare.html

cleanExtra:
	rm -rf xml html ../ejs.tags

clobberExtra:
	rm -f ../ejs.html ../ejsBare.html ../mpr.html

#
#   Local variables:
#   tab-width: 4
#   c-basic-offset: 4
#   End:
#   vim: sw=4 ts=4 noexpandtab
#
