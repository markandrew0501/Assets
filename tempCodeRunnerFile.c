#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

void cleanup_handler(void *arg) {
    printf("[Worker] Cleaning up: %s\n", (char *)arg);
}

//Asynchronous Cancellation
void *worker_async(void *arg) {
    int count = 0;

    pthread_cleanup_push(cleanup_handler, "Releasing resources (ASYNC)...");

    printf("[Worker] Running with ASYNCHRONOUS cancellation.\n");
    pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);

    while (1) {
        printf("[Worker] Count = %d\n", count++);
        usleep(200000); // sleep for 0.2s
        printf("[Worker] STILL IN LOOP \n");

    }

    pthread_cleanup_pop(1); // Execute cleanup if reached
    return NULL;
}

//Deferred Cancellation
void *worker_deferred(void *arg) {
    int count = 0;

    // Register cleanup handler
    pthread_cleanup_push(cleanup_handler, "Releasing resources (DEFERRED)...");

    printf("[Worker] Running with DEFERRED cancellation.\n");
    pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED, NULL);

    while (1) {
        printf("[Worker] BEFORE TEST CANCEL\n");
        printf("[Worker] Count = %d\n", count++);
        usleep(200000); // sleep for 0.2s
        pthread_testcancel(); // Check for cancellation
        printf("[Worker] AFTER TEST CANCEL\n");
    }

    pthread_cleanup_pop(1); // Execute cleanup if reached
    return NULL;
}

int main(void) {
    pthread_t worker;

    printf("\nAsynchronous Cancellation\n");
    pthread_create(&worker, NULL, worker_async, NULL);
    sleep(1); 
    printf("[Main] Requesting cancellation (ASYNCHRONOUS)\n");
    pthread_cancel(worker);
    pthread_join(worker, NULL);
    printf("[Main] Worker thread terminated (ASYNC).\n");

    printf("\nDeferred Cancellation\n");
    pthread_create(&worker, NULL, worker_deferred, NULL);
    sleep(1); // Let worker run
    printf("[Main] Requesting cancellation (DEFERRED)...\n");
    pthread_cancel(worker);
    pthread_join(worker, NULL);
    printf("[Main] Worker thread terminated (DEFERRED).\n");

    return 0;
}
