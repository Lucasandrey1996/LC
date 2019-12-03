CC = gcc
CFLAGS = -Wall -Wextra -g
LDFLAGS=-lm
EXEC=makeExo3

SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
DEP = $(OBJ:.o=.d)

all: $(EXEC)

.PHONY: clean
clean:
	rm -f *.i *.s *.o *.d $(EXEC)

print-%:
	@echo $* = $($*)

-include $(DEP)

$(EXEC): $(OBJ)
	$(CC) $^ -o $(EXEC)
	$(CC) $^ $(LDFLAGS) -Wl,-Map,main.map -o  $@

%.o: %.c
	$(CC) -o $@ -c -MMD $*.c ${CFLAGS}
	$(CC) -E $< -o $*.i ${CFLAGS}
	$(CC) -S $< -o $*.s ${CFLAGS}
