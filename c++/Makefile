TARGET=main
SOURCES=$(TARGET).cpp
OBJECTS=$(SOURCES:.cpp=.o)
CC=g++
CXX_FLAGS=-c -Wall
CXX_DEBUG_FLAGS=-DDEBUG
CXX_LINT=cpplint.py
LD_FLAGS=

all: $(LINT) $(TARGET)

.PHONY: debug lint clean test

debug: CXX_FLAGS+=$(CXX_DEBUG_FLAGS)
debug: $(LINT) $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(LD_FLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CXX_FLAGS) $< -o $@

lint:
	${CXX_LINT} ${SOURCES}

clean:
	rm -f $(TARGET)
	rm -f *.o

test: $(LINT) $(TARGET)
	@echo "== Test 1 =="
	@./$(TARGET) < test1
