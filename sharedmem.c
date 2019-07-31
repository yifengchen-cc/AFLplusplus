/*

 */

#define AFL_MAIN

#include "config.h"
#include "types.h"
#include "debug.h"
#include "alloc-inl.h"
#include "hash.h"
#include "sharedmem.h"

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#include <signal.h>
#include <dirent.h>
#include <fcntl.h>

#include <sys/wait.h>
#include <sys/time.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/resource.h>
#include <sys/mman.h>

#ifndef USEMMAP
 #include <sys/ipc.h>
 #include <sys/shm.h>
#endif

extern unsigned char*trace_bits;

static s32 piper[2];

void remove_shm(void) {
  close(piper[0]);
}


/* Configure shared memory. */

void setup_shm(unsigned char dumb_mode) {
  if (pipe(piper) != 0)
    PFATAL("pipe() failed");
}
