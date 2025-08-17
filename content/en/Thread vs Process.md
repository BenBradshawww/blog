+++
title = 'Thread vs Process'
date = 2025-05-11
categories = ["Programming"]
tags = ["Programming"]
keywords = ["Programming"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image by Ammar Mahmood](/images/ammar-mahmood-NkB27DjRE7Y-unsplash.jpg)
[Image by Ammar Mahmood](https://unsplash.com/@ammarmahmood)

## What is a Process?

A process is an instance of a program that is running on a computer. Each computer has its own memory space, system resources, and execution context. For example, when you run a piece of code, create a new browser tab, or open a new application, you are creating a new process. [1]

Some of the characteristics a process include:
1. Isolation. Each process runs independently and lives in an isolated space from other processes. This isolation makes processes fault tolerant where the failure of one process will not impact the success of the remaining processes.
2. Heavyweight. Processes require more resources and overhead to create and manage because they have their own memory space. As a result, the memory between different processes cannot be shared.
3. Communication. Processes communicate with each other using inter-process communication (IPC) mechanisms like pipes, sockets, and shared memory. These processes are slow when compared to the threads.

In Python, you can use the higher level package called `concurrent.futures` to create subprocesses for a task. By calling `concurrent.futures.ProcessPoolExecutor`, the executor will use the multiprocessing module, allowing the module to side-step the Global Interpreter Lock (GIL). However, this only means that pickable objects can be executed or returned.

```python
import concurrent.futures
import math

PRIMES = [
112272535095293,
112582705942171,
112272535095293,
115280095190773,
115797848077099,
1099726899285419,
]

def is_prime(n):
if n < 2:
return False
if n == 2:
return True
if n % 2 == 0:
return False

sqrt_n = int(math.floor(math.sqrt(n)))
for i in range(3, sqrt_n + 1, 2):
if n % i == 0:
return False
return True

def main():
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
main()
```

The script above will determine whether an inputted list of numbers are prime or not.

It's worth mentioning, the `if __name__ == "__main__":` is essential here. If this line is disregarded, this error will be thrown: `RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase`.

When python creates a new process, it'll start a fresh Python interpreter and imports the script as a module. If it imports the script without the `if __name__ == "__main__":` safeguard, the script will iteratively import the main script again, and run again and create a new Python interpreter. By putting the safeguard, it stops the guarded block from running in the child and prevents accidental process creation before bootstrapping is complete.

## What is a Thread?

A thread is smaller unit of execution within a process. Multiple threads within the same process use the same memory space and resources allowing for a more efficient communication and data sharing. Often, threads are called "lightweight processes".

Some of the characteristics of a thread include:
1. Shared Memory. Threads within a shared process share the same memory and resources, allowing for fast communications. Additionally, it allows the threads to read and write from the same variables and data structures.
2. Lightweight. Threads are easier and faster to create and manage compared to processes. As a result, they are easier to create and destroy.
3. Concurrency. Multiple threads within the same process can run concurrently, allowing tasks to make progress independently. On multi-core processors, this can also enable true parallel execution of tasks.
4. Lack of isolation. Since the threads are not isolated from each other and share the same resources, there may result in issues such as data races and deadlocks if the threads are not managed correctly.

Example:
1. When a web browser is run, threads work behind the scenes to handle different tasks at the same time. One thread will load the webpage content, this includes text, images, and videos. Another thread will respond to your actions on the page. Another thread will run the JavaScript to make the page interactive. If threads were not used in a browser, the browser would freeze as it waits for one task to finish before starting another. Threads ensure everything is fast and seamless. [2]

Additional Notes:
1. Threads are not the same as child processes. Child processes are separate processes that are created by a parent process and has it's own memory and resources.
2. Threads share pre-process items such as address space, global variables, open files, child processes, pending alarms, signals, signal handlers, and accounting information. However, each thread has it's own private resources including program counter, registers, stack, and state.

In Python, you could implement multithreading with the `ThreadPoolExecutor` from the `Executor` subclass that uses a pool of threads to execute calls asynchronously. Once submitted, these tasks are sent to run in the background on multiple threads.

```python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
'http://www.cnn.com/',
'http://europe.wsj.com/',
'http://www.bbc.co.uk/',
'http://nonexistent-subdomain.python.org/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
with urllib.request.urlopen(url, timeout=timeout) as conn:
return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
# Start the load operations and mark each future with its URL
future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
for future in concurrent.futures.as_completed(future_to_url):
url = future_to_url[future]
try:
data = future.result()
except Exception as exc:
print('%r generated an exception: %s' % (url, exc))
else:
print('%r page is %d bytes' % (url, len(data)))
```

For more details about the module `concurrent.futures`, please read the appendix.
## Definitions:

1. Program: A program is a set of instructions written in a programming language that tells a computer how to perform a task. These programs are typically stored in a file and must be executed by a computer or VM to produce the results.
2. Context Switching: This is the process of storing the state of a process and restoring the state of another process to resume execution. This is managed by the OS and it is necessary for multitasking.
3. Data Races: A data race occurs when two or more threads access the same memory location concurrently and at least one of the threads modifies the data. Without proper synchronisation (such as locks and mutexes) the value of the accessed object may be incorrect.
4. Deadlocks: A deadlock occurs when two or more process wait indefinitely for resources held by each other. As a result, none of them proceed with their process. The conditions for a deadlock are known as "The Coffman Conditions". For example, a deadlock occurs when process A holds on resource 1 and waits for resource 2, but process B holds resources 2 and is waiting on resource 1.
5. IPC. Inter-Process Communication refers to the mechanism used by operating systems to allow processes to communicate with each other. The IPC is used for coordination, data sharing, modularity, and to improve performance. There are many different IPC mechanisms, with each one suited for different scenarios. Some of the common ones include: pipes, named pipes, message queues, shared memory, sockets, signals, rpcs and more.

## References:
1. i.vikash (2024). _Difference Between a Process and a Thread (With Real-Life Examples)_. [online] Medium. Available at: https://medium.com/@i.vikash/difference-between-a-process-and-a-thread-with-real-life-examples-deeaed6b27f8 [Accessed 24 Jan. 2025].
2. GeeksforGeeks (2019). _Difference between Process and Thread_. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/difference-between-process-and-thread/.
3. docs.python.org. (n.d.). _concurrent.futures — Launching parallel tasks — Python 3.9.5 documentation_. [online] Available at: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.


## Appendix

**concurrent.futures**

This sends a task (either a thread or process) to run in the background. Instead of blocking the script from continuing, a `Future` object is returned immediately.

A Future is a concurrency primitive representing a result that may not yet be available. Executors return futures when you submit work. You can poll, wait for, or attach callbacks to them, allowing you to manage results of concurrent tasks without blocking immediately.

Some of the `Future` methods are:
* `cancel()`: This attempts to cancel the call.
* `cancelled()`: Returns `True` if the call was cancelled.
* `running()`: Returns `True` is the call is currently being executed and cannot be cancelled.
* `done()`: Returns `True` is
* `result(timeout=None)`: Returns the value returned by the call.

‌
