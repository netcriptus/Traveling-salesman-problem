SRC=src/tsp-dp.py
LINK=tsp-dp

all:
	chmod a+x ${SRC}
	ln -s ${SRC} ${LINK}

clean:
	rm -rf ${LINK}
	chmod a-x ${SRC}